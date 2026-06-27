from groq import Groq

from config import GROQ_API_KEY, AI_MODELS
from providers.provider_error import (
    ProviderUnavailable,
    InvalidAPIKey,
)


client = Groq(api_key=GROQ_API_KEY)


def generate_response(prompt: str) -> str:

    try:

        response = client.chat.completions.create(
            model=AI_MODELS["groq"],
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        error = str(e).lower()

        if "authentication" in error or "api key" in error:
            raise InvalidAPIKey("Groq API key is invalid.")

        raise ProviderUnavailable(str(e))