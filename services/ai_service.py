from config import AI_PROVIDER_ORDER

from providers import gemini
from providers import openrouter
from providers import groq


# ==========================================
# Monday Personality
# ==========================================

SYSTEM_PROMPT = """
You are Monday.

You are an intelligent AI assistant that lives inside a Discord server.

Rules:
- Never say you are Gemini, ChatGPT, Groq, or any AI model.
- If asked who created you, reply:
  "I was created and moderated by AriesX."
- Keep replies short and conversational unless the user asks for detail.
- Use the provided Discord context as factual information.
- Never say you cannot access Discord if the information exists in the context.
- Speak naturally like another member of the server.
"""


# ==========================================
# Provider Dictionary
# ==========================================

PROVIDERS = {
    "gemini": gemini,
    "openrouter": openrouter,
    "groq": groq
}


# ==========================================
# Main AI Function
# ==========================================

def ask_ai(context, prompt):

    full_prompt = f"""
{SYSTEM_PROMPT}

==========================
DISCORD CONTEXT
==========================

{context}

==========================
USER MESSAGE
==========================

{prompt}
"""

    last_error = None

    for provider_name in AI_PROVIDER_ORDER:

        provider = PROVIDERS.get(provider_name)

        if provider is None:
            continue

        try:
            print(f"[AI] Trying provider: {provider_name}")

            response = provider.generate_response(full_prompt)

            print(f"[AI] Success using: {provider_name}")

            return response

        except Exception as e:

            print(f"[AI] {provider_name} failed.")

            print(e)

            last_error = e

            continue

    return (
        "⚠️ Sorry, all AI providers are currently unavailable.\n"
        f"Last Error: {last_error}"
    )