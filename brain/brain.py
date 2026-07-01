from brain.intent import detect
from brain.planner import execute
from services.intent_service import classify
from services.logger import info

class MondayBrain:

    async def think(self, ctx, prompt):

        intent = detect(prompt)

        if intent is None:
            intent = classify(prompt)

        info(f"[Brain] Intent: {intent.name}")

        return await execute(intent, ctx, prompt)