🤖 Monday

An AI-powered Discord assistant that thinks before it speaks.

Monday is a modular Discord AI assistant built around a Brain → Planner → Skills architecture. Instead of sending every request directly to a language model, Monday analyzes the user's intent, selects the appropriate skill or tool, gathers context when needed, and only uses AI when it's the best solution.

Designed with scalability in mind, Monday combines AI conversation, Discord server intelligence, moderation, memory, and internet tools into one extensible assistant.

✨ Features
🧠 AI Brain
Intent-based request routing
Brain → Planner → Skills architecture
AI-assisted conversations
Context-aware responses
Modular skill system
🤖 Multi-Provider AI

Supported providers:

Google Gemini
OpenRouter
Groq

Features:

Automatic provider failover
Configurable provider priority
Unified AI interface
Easy provider expansion
💬 Conversation Intelligence
Reads recent Discord conversations
Context-aware replies
Conversation history (RAG)
Chat summarization
🧠 Long-Term Memory

Monday can remember user preferences.

Examples:

Remember that my favorite IDE is VS Code.

What's my favorite IDE?

Forget my favorite IDE.
🌐 Internet Tools

Built-in tools include:

Wikipedia
Weather
GitHub Repository Search
Web Search
Calculator
UUID Generator
Date & Time

Tools are only used when appropriate—general knowledge questions still go to the AI.

👤 Discord Intelligence
User
Username
Nickname
Avatar
Roles
User ID
Join Date
Account Creation
Boost Status
Server
Member Count
Owner
Roles
Statistics
Channel
Topic
Slowmode
Pinned Messages
Analytics
Most Active Members
Chat Activity
Conversation Summary
🛡️ Moderation

AI-powered moderation commands:

Kick
Ban
Timeout
Unban
Purge
Warnings

Includes:

Permission validation
Role hierarchy protection
Moderation logging
📝 Logging
Console logging
Daily log files
Configurable Discord log channel
Moderation action logging

⚙️ Architecture
                    User

                      │

                      ▼

                Monday Brain

                      │

               Intent Detection

                      │

                      ▼

                  Planner

        ┌────────┬─────────┬──────────┬──────────┐
        │        │         │          │
        ▼        ▼         ▼          ▼

   Discord     Memory     Tools      AI

        │                    │

        ▼                    ▼

   Discord API         AI Providers

                  ┌─────────┬─────────┬─────────┐
                  │         │         │
                  ▼         ▼         ▼

               Gemini     Groq   OpenRouter


📂 Project Structure
Monday/

├── brain/
├── cogs/
├── providers/
├── services/
├── skills/
│   ├── discord/
│   └── moderation/
├── tools/
│   └── internet/
├── utils/

├── MondayMain.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md


🚀 Installation
Clone the repository

git clone https://github.com/dev-aj-5/Monday.git

Move into the project

cd Monday

Install dependencies

pip install -r requirements.txt

Create a .env file:

DISCORD_TOKEN=

GEMINI_API_KEY=

OPENROUTER_API_KEY=

GROQ_API_KEY=

Run Monday

python MondayMain.py

💬 Example Commands
AI
!ask Hello Monday

!ask Explain quantum computing
Memory
!ask Remember that my favorite IDE is VS Code

!ask What's my favorite IDE?

!ask Forget my favorite IDE.
Discord
!ask What's my avatar?

!ask Who owns this server?

!ask Who talks the most?
Moderation
!ask Kick @User

!ask Timeout @User

!ask Warn @User Spamming

!ask Purge 10
Internet
!ask Weather in London

!ask Wikipedia Python

!ask GitHub discord.py

!ask Generate UUID
🛠 Tech Stack
Python 3.14
discord.py
Google Gemini API
Groq API
OpenRouter API
SQLite
Requests
python-dotenv
🛣 Roadmap
✅ Version 1.0
Brain Architecture
Planner
Intent Detection
Multi-provider AI
Conversation Context
Memory
Discord Skills
Moderation System
Internet Tools
Logging
Guild Settings
🚀 Version 2.0
Web Dashboard
Discord OAuth2
Docker Support
24/7 Cloud Hosting
Auto Moderation
Plugin System
Web UI
Slash Commands
🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the project, open an issue, or submit a pull request.

📜 License

This project is licensed under the MIT License.

💡 Philosophy

Most Discord AI bots simply forward prompts to a language model.

Monday follows a different philosophy.

Every request first passes through a Brain, which determines the user's intent, chooses the appropriate skill or tool, gathers any required context, and only consults an AI model when necessary.

The goal is to build an assistant that is intent-driven, modular, and extensible—one that doesn't just generate responses, but makes informed decisions before responding.