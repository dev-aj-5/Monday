from brain.intent import Intent

from skills.discord_skill import handle as discord_handle

from services.ai_service import ask_ai
from services.context_service import build_context
from services.conversation_service import answer_from_history


async def execute(intent, ctx, prompt):

    # -------------------------
    # Discord Knowledge
    # -------------------------

    if intent in [

        Intent.USER_INFO,

        Intent.SERVER_INFO,

        Intent.CHANNEL_INFO,

        Intent.BOT_INFO

    ]:

        answer = await discord_handle(ctx, prompt)

        if answer is not None:
            return answer

    # -------------------------
    # Conversation
    # -------------------------

    if intent == Intent.CONVERSATION:

        return await answer_from_history(
            ctx,
            prompt
        )

    # -------------------------
    # Memory
    # -------------------------

    if intent == Intent.MEMORY:

        return "Memory service hasn't been built yet."

    # -------------------------
    # Moderation
    # -------------------------

    if intent == Intent.MODERATION:

        return "Moderation service hasn't been built yet."

    # -------------------------
    # Default AI
    # -------------------------

    context = build_context(ctx)

    return ask_ai(context, prompt)