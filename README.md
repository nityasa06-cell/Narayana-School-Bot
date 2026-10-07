# Narayana School Chatbot

A simple chatbot for **Narayana School, Kalimpong**, powered by the Groq API and Flask.

---

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Add your Groq API key

Open the `.env` file and replace the placeholder with your actual key:

```
GROQ_API_KEY=your_actual_api_key_here
```

Get a free key at [console.groq.com/keys](https://console.groq.com/keys).

---

## 3. Run locally

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

---

## 4. Where to edit the system prompt and personalization

Everything is in **`app.py`**, in the `SYSTEM_PROMPT` variable near the top of the file.

It is divided into clearly labelled sections:

| Section | What to edit |
|---|---|
| `COLLABORATORS` | Names of people who worked on the chatbot |
| `FRIENDS` | Information about your friends |
| `CREATOR` | Information about who made it |
| `BEHAVIOR` | How the bot should behave and respond |

Just edit the text inside the triple-quoted string — no other files need to change.

---

## 5. Deploy to Vercel

### Prerequisites
- A [Vercel](https://vercel.com) account
- [Vercel CLI](https://vercel.com/docs/cli) installed: `npm i -g vercel`

### Steps

**Option A — via Vercel CLI:**
```bash
vercel
```
Follow the prompts. When asked about environment variables, add `GROQ_API_KEY`.

**Option B — via Vercel Dashboard (recommended):**
1. Push this repo to GitHub
2. Go to [vercel.com/new](https://vercel.com/new)
3. Import your GitHub repository
4. Under **Environment Variables**, add:
   - Key: `GROQ_API_KEY`
   - Value: your Groq API key
5. Click **Deploy**

> ⚠️ **Never commit your `.env` file.** It is already excluded by `.gitignore`.
> On Vercel, always set `GROQ_API_KEY` via the Vercel dashboard under Project → Settings → Environment Variables.

---

## Project structure

```
globebot/
├── app.py              ← Flask backend + Groq integration + system prompt
├── vercel.json         ← Vercel deployment configuration
├── .env                ← Your API key (never share or commit this)
├── requirements.txt    ← Python dependencies
├── templates/
│   └── index.html      ← Chat frontend (HTML/CSS/JS)
└── README.md
```
