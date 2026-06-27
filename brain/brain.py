from brain.intent import detect
from brain.planner import execute
from services.intent_service import classify


class MondayBrain:

    async def think(self, ctx, prompt):

        intent = detect(prompt)

        if intent is None:
            intent = classify(prompt)

        print(f"[Brain] Intent: {intent.name}")

        return await execute(intent, ctx, prompt)