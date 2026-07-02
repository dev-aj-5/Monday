
# ===========================
# MONDAY BOT CONFIG
# ===========================
import os
from version import VERSION, CODENAME, BUILD
from dotenv import load_dotenv
MODE = os.getenv("MODE", "development")
load_dotenv()

BOT_NAME = "Monday"
BOT_VERSION = VERSION
BOT_CODENAME = CODENAME
BOT_BUILD = BUILD
DISCORD_PREFIX = "!"
# AI Providers (Priority Order)
AI_PROVIDER_ORDER = [
    "gemini",
    "groq",
    "openrouter"
]

# Models
AI_MODELS = {
    "gemini": "gemini-2.5-flash",
    "openrouter": "openrouter/free",
    "groq": "llama-3.3-70b-versatile"
}

# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Discord
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


import os

MODE = os.getenv("MODE", "development")

DEBUG = MODE == "development"

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")