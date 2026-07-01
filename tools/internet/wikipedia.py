import requests


API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"


def search_wikipedia(prompt):

    query = prompt.lower()

    # Remove common phrases
    for phrase in [
        "wiki",
        "wikipedia",
        "who is",
        "what is",
        "what are",
        "tell me about",
        "explain"
    ]:
        query = query.replace(phrase, "")

    query = query.replace("?", "").strip()

    if not query:
        return "Please tell me what you want to search."

    query = query.replace(" ", "_")

    try:

        response = requests.get(
            API_URL + query,
            headers={
                "User-Agent": "MondayBot/1.0"
            },
            timeout=10
        )

        if response.status_code != 200:
            return "I couldn't find that Wikipedia article."

        data = response.json()

        title = data.get("title", "Unknown")

        extract = data.get(
            "extract",
            "No summary available."
        )

        return (
            f"📚 **{title}**\n\n"
            f"{extract}"
        )

    except requests.exceptions.Timeout:
        return "Wikipedia took too long to respond."

    except requests.exceptions.RequestException:
        return "I couldn't reach Wikipedia."

    except Exception as e:
        return f"Wikipedia Error: {e}"