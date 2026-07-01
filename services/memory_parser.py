import re


def parse_memory(prompt: str):

    # Keep original capitalization for values
    original_prompt = prompt

    # Lowercase only for matching
    prompt = prompt.lower()

    # --------------------------------------------------
    # Favorite
    # --------------------------------------------------

    match = re.search(
        r"remember that my favorite (.+?) is (.+)",
        original_prompt,
        re.IGNORECASE
    )

    if match:

        thing = (
            match.group(1)
            .replace("?", "")
            .replace(".", "")
            .replace("!", "")
            .strip()
            .lower()
        )

        value = (
            match.group(2)
            .replace("?", "")
            .replace(".", "")
            .replace("!", "")
            .strip()
        )

        return {
            "category": "preferences",
            "key": f"favorite_{thing.replace(' ', '_')}",
            "value": value
        }

    return None