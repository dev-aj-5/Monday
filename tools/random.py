import random
import re


def handle_random(prompt):

    prompt = prompt.lower()

    if "coin" in prompt:
        return random.choice(["Heads", "Tails"])

    dice = re.search(r"d(\d+)", prompt)

    if dice:

        sides = int(dice.group(1))

        return str(random.randint(1, sides))

    between = re.search(
        r"between (\d+) and (\d+)",
        prompt
    )

    if between:

        low = int(between.group(1))
        high = int(between.group(2))

        return str(random.randint(low, high))

    return None