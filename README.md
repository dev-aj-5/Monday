# 🤖 Monday

> **An AI assistant that thinks before it speaks.**

Monday is a modular AI-powered Discord assistant built around a **Brain → Planner → Skills** architecture instead of sending every request directly to an LLM.

It understands user intent, routes requests to specialized services, remembers recent conversations through Retrieval-Augmented Generation (RAG), and automatically switches between multiple AI providers when one becomes unavailable.

---

# ✨ Features

## 🧠 Intelligent Brain

* Intent-based request routing
* AI-assisted intent classification
* Central planner for task execution
* Modular architecture for future expansion

## 💬 Conversation Awareness

* Reads recent Discord conversations
* Builds conversation context
* Answers questions using recent chat history (RAG)
* Conversation summarization

## 🤖 Multi-Provider AI

* Google Gemini
* Groq
* OpenRouter

Features include:

* Automatic provider failover
* Configurable provider priority
* Unified AI interface

## 👤 Discord Knowledge

Monday understands Discord itself.

Current supported knowledge includes:

* User information
* Server information
* Channel information
* Bot information

## ⚙️ Architecture

Designed around independent services instead of one large bot file.

```
User

    │

    ▼

 Monday Brain

    │

Intent Detection

    │

    ▼

 Planner

    │

 ┌───────────────┬────────────────┬──────────────┐
 │               │                │
 ▼               ▼                ▼

Discord      Conversation      AI Chat
 Skills           RAG

        │

        ▼

     AI Manager

 ┌──────────┬──────────┬──────────────┐
 │          │          │
 ▼          ▼          ▼

Gemini     Groq    OpenRouter
```

---

# 📂 Project Structure

```
Monday/

├── brain/
│   ├── brain.py
│   ├── planner.py
│   └── intent.py
│
├── cogs/
│
├── providers/
│
├── services/
│
├── skills/
│
├── utils/
│
├── config.py
├── MondayMain.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/dev-aj-5/Monday.git
```

Move into the project:

```bash
cd Monday
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example` and add your own API keys:

```
DISCORD_TOKEN=

GEMINI_API_KEY=

GROQ_API_KEY=

OPENROUTER_API_KEY=
```

Run the bot:

```bash
python MondayMain.py
```

---

# ⚙️ Configuration

Provider priority can be configured inside `config.py`.

Example:

```python
AI_PROVIDER_ORDER = [
    "gemini",
    "groq",
    "openrouter"
]
```

Changing the order automatically changes which provider Monday prefers.

---

# 🛣️ Roadmap

## ✅ Completed

* Brain Architecture
* Planner
* Intent Detection
* AI Provider Manager
* Automatic AI Failover
* Discord Knowledge Skills
* Conversation RAG
* Asynchronous Architecture
* GitHub Ready Configuration

## 🚧 In Progress

* Long-Term Memory
* Tool Calling
* Web Search
* Mention Mode
* Multi-step Planning

---

# 🛠️ Tech Stack

* Python 3.14
* discord.py
* Google Gemini API
* Groq API
* OpenRouter API
* python-dotenv
* Requests

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

If you'd like to improve Monday, feel free to fork the repository and open a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 💡 Philosophy

Most Discord AI bots simply forward prompts to a language model.

Monday takes a different approach.

Every request first passes through a **Brain**, which understands the user's intent, selects the appropriate skill or service, gathers any required context, and only then asks an AI model when necessary.

The goal is to build an assistant that doesn't just generate responses—but **thinks before it speaks**.
