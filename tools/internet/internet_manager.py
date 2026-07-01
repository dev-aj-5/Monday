from tools.internet.web_search import search_web
from tools.internet.wikipedia import search_wikipedia
from tools.internet.weather import get_weather
from tools.internet.github import github_search


def handle_internet(prompt):

    prompt_lower = prompt.lower()

    # ----------------------------
    # Weather
    # ----------------------------

    if (
        "weather" in prompt_lower
        or "temperature" in prompt_lower
        or "forecast" in prompt_lower
    ):
        return get_weather(prompt)

    # ----------------------------
    # GitHub
    # ----------------------------

    if (
        "github" in prompt_lower
        or "repository" in prompt_lower
        or "repo" in prompt_lower
    ):
        return github_search(prompt)

    # ----------------------------
    # Wikipedia
    # ----------------------------

    if (
        prompt_lower.startswith("wiki")
        or "who is" in prompt_lower
        or "what is" in prompt_lower
        or "what are" in prompt_lower
        or "tell me about" in prompt_lower
        or "explain" in prompt_lower
    ):
        return search_wikipedia(prompt)

    # ----------------------------
    # Web Search
    # ----------------------------

    if prompt_lower.startswith("search "):
        return search_web(prompt)

    return None