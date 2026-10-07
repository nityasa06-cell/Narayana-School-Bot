import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# ---------------------------------------------------------------------------
# SYSTEM PROMPT
# Edit this section to customize the chatbot's behavior and personalization.
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """
You are the Narayana School Assistant for Narayana School, Kalimpong.
Your job is to help answer questions related to Narayana School, its academics,
campus, students, activities, rules, schedules, facilities, and other
school-related topics.

---

PERSONALIZATION

Use the following information only when it is relevant to the conversation.
Do not bring it up unless it fits naturally.

---

COLLABORATORS

I worked on this chatbot with:
- Ethan
- Tesha
- Nishant

---

FRIENDS

[Add information about friends here when needed.]

---

CREATOR

This chatbot was created by me.
[Add more creator details here when needed.]

---

BEHAVIOR

- Be helpful and conversational.
- Keep answers clear and easy to understand.
- Do not invent information about Narayana School.
- If you do not know something, say that you don't know rather than making up an answer.
- Use the personalization information naturally rather than mentioning it unnecessarily.
- Answer the user's actual question directly.
- Keep responses concise unless the user asks for more detail.
"""

# ---------------------------------------------------------------------------
# Groq setup
# ---------------------------------------------------------------------------

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY environment variable is not set. Add it to your .env file.")

client = Groq(api_key=GROQ_API_KEY)
MODEL = "openai/gpt-oss-20b"

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Serve the main chat page."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """
    Receive the conversation history from the frontend,
    send it to Groq, and return the assistant's reply.

    Expected request body (JSON):
    {
        "history": [
            {"role": "user",      "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"},
            ...
        ],
        "message": "What classes are offered?"
    }
    """
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided."}), 400

    user_message = data["message"].strip()
    history = data.get("history", [])

    if not user_message:
        return jsonify({"error": "Message is empty."}), 400

    # Build the messages list: system prompt + conversation history + new message
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for entry in history:
        messages.append({
            "role": entry["role"],       # "user" or "assistant"
            "content": entry["content"]
        })

    messages.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
        )
        reply = response.choices[0].message.content
    except Exception as e:
        return jsonify({"error": f"Groq API error: {str(e)}"}), 500

    return jsonify({"reply": reply})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
