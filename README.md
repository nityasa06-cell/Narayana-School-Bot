# Narayana School Chatbot

A simple chatbot for **Narayana School, Kalimpong**, powered by the Gemini API and Flask.

---

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Add your Gemini API key

Open the `.env` file and replace the placeholder with your actual key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

Get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## 3. Run the application

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

---

## 4. Where to edit the system prompt and personalization

Everything is in **`app.py`**, in the `SYSTEM_PROMPT` variable near the top of the file (around line 15).

It is divided into clearly labelled sections:

| Section | What to edit |
|---|---|
| `PERSONALIZATION` | General intro to personalization |
| `COLLABORATORS` | Names of people who worked on the chatbot |
| `FRIENDS` | Information about your friends |
| `CREATOR` | Information about who made it |
| `BEHAVIOR` | How the bot should behave and respond |

Just edit the text inside the triple-quoted string — no other files need to change.

---

## Project structure

```
globebot/
├── app.py              ← Flask backend + Gemini integration + system prompt
├── .env                ← Your API key (never share this file)
├── requirements.txt    ← Python dependencies
├── templates/
│   └── index.html      ← Chat frontend (HTML/CSS/JS)
└── README.md
```
