from google import genai

from config import GEMINI_API_KEY, AI_MODELS
from providers.provider_error import (
    ProviderUnavailable,
    InvalidAPIKey,
)

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt: str) -> str:
    try:

        response = client.models.generate_content(
            model=AI_MODELS["gemini"],
            contents=prompt
        )

        return response.text

    except Exception as e:

        error = str(e)

        if "429" in error:
            raise ProviderUnavailable("Gemini rate limit exceeded.")

        if "503" in error:
            raise ProviderUnavailable("Gemini service unavailable.")

        if "401" in error or "403" in error:
            raise InvalidAPIKey("Gemini API key is invalid.")

        raise ProviderUnavailable(error)