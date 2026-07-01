import requests


API_URL = "https://api.github.com/search/repositories"


def github_search(prompt):

    query = prompt.lower()

    query = query.replace("github", "")
    query = query.replace("search", "")
    query = query.strip()

    if not query:
        return "Tell me what GitHub repository you want to search."

    try:

        response = requests.get(

            API_URL,

            params={
                "q": query,
                "per_page": 5
            },

            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "MondayBot"
            },

            timeout=10
        )

        if response.status_code != 200:
            return "GitHub search failed."

        data = response.json()

        items = data.get("items", [])

        if not items:
            return "No repositories found."

        result = "🐙 **Top GitHub Results**\n\n"

        for repo in items:

            result += (
                f"**{repo['full_name']}**\n"
                f"⭐ {repo['stargazers_count']:,} stars\n"
                f"{repo['html_url']}\n\n"
            )

        return result

    except Exception as e:

        return f"GitHub Error:\n{e}"