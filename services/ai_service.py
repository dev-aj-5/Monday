from config import AI_PROVIDER_ORDER

from providers import gemini
from providers import openrouter
from providers import groq

from brain.personality import SYSTEM_PROMPT
from services.logger import info
from services.logger import error
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
            info(f"[AI] Trying provider: {provider_name}")

            response = provider.generate_response(full_prompt)

            info(f"[AI] Success using: {provider_name}")

            return response

        except Exception as e:

            error(f"[AI] {provider_name} failed.")

            error(f"[AI] Error: {e}")

            last_error = e

            continue

    return (
        "⚠️ Sorry, all AI providers are currently unavailable.\n"
        f"Last Error: {last_error}"
    )