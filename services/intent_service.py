from brain.intent import Intent
from services.ai_service import ask_ai


def classify(prompt: str) -> Intent:

    system_prompt = f"""
You are Monday's intent classifier.

Choose ONE intent.

USER_INFO
SERVER_INFO
CHANNEL_INFO
BOT_INFO
CONVERSATION
MEMORY
MODERATION
AI_CHAT

Definitions:

USER_INFO:
Questions about users, avatars, IDs, nicknames, roles.

SERVER_INFO:
Questions about the Discord server.

CHANNEL_INFO:
Questions about channels.

BOT_INFO:
Questions about Monday itself.

CONVERSATION:
Questions that require reading recent Discord messages.
Examples:
- What did I buy?
- Which watch did I buy?
- What were we discussing?
- Summarize the chat.
- Who said...

MEMORY:
Long-term remembered information.

MODERATION:
Kick, ban, timeout, mute.

AI_CHAT:
Everything else.

Return ONLY ONE WORD.

Prompt:
{prompt}
"""

    result = ask_ai("", system_prompt).strip().upper()

    try:
        return Intent[result]
    except KeyError:
        return Intent.AI_CHAT