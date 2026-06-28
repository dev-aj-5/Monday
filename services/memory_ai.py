import json

from services.ai_service import ask_ai


def extract_memories(context, prompt):

    system_prompt = """
You extract memories from user messages.

Return ONLY valid JSON.

Format:

{
    "memories":[
        {
            "category":"preferences",
            "key":"favorite_editor",
            "value":"VS Code"
        }
    ]
}

Rules:

- Only extract long-term facts.
- Ignore temporary requests.
- If nothing should be remembered:

{
    "memories":[]
}
"""

    response = ask_ai(
        context,
        system_prompt + "\n\nUser:\n" + prompt
    )

    try:

        return json.loads(response)

    except Exception:

        return {
            "memories": []
        }