import requests
import json
from config import OPENROUTER_API_KEY, AI_MODELS
from providers.provider_error import (
    ProviderUnavailable,
    InvalidAPIKey,
)


URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_response(prompt: str) -> str:

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/avi/monday",
        "X-Title": "Monday Discord Bot"
    }

    payload = {
        "model": AI_MODELS["openrouter"],
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        if response.status_code == 401:
            raise InvalidAPIKey("OpenRouter API key is invalid.")

        if response.status_code == 429:
            raise ProviderUnavailable("OpenRouter rate limit exceeded.")

        if response.status_code >= 500:
            raise ProviderUnavailable("OpenRouter server unavailable.")

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        raise ProviderUnavailable("OpenRouter request timed out.")

    except requests.exceptions.ConnectionError:
        raise ProviderUnavailable("Could not connect to OpenRouter.")

    except Exception as e:
        raise ProviderUnavailable(str(e))