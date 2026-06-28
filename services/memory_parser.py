import re


def parse_memory(prompt: str):

    prompt = prompt.lower()

    # Favorite X

    match = re.search(
        r"remember that my favorite (.+?) is (.+)",
        prompt,
        re.IGNORECASE
    )

    if match:

        thing = match.group(1).strip()
        value = match.group(2).strip()

        return {
            "category": "preferences",
            "key": f"favorite_{thing.replace(' ', '_')}",
            "value": value
        }

    return None