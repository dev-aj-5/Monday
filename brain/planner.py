from brain.intent import Intent

from skills.discord_skill import handle as discord_handle

from services.ai_service import ask_ai
from services.context_service import build_context
from services.conversation_service import answer_from_history

from services.memory_service import (
    remember,
    recall,
    forget
)

from services.memory_parser import parse_memory

from tools.tool_manager import handle_tool

import re


async def execute(intent, ctx, prompt):

    prompt_lower = prompt.lower()

    # --------------------------------------------------
    # Discord Knowledge
    # --------------------------------------------------

    if intent in [
        Intent.USER_INFO,
        Intent.SERVER_INFO,
        Intent.CHANNEL_INFO,
        Intent.BOT_INFO
    ]:

        answer = await discord_handle(ctx, prompt)

        if answer is not None:
            return answer

    # --------------------------------------------------
    # Conversation
    # --------------------------------------------------

    elif intent == Intent.CONVERSATION:

        return await answer_from_history(
            ctx,
            prompt
        )

    # --------------------------------------------------
    # Memory
    # --------------------------------------------------

    elif intent == Intent.MEMORY:

        # ----------------------------
        # STORE
        # ----------------------------

        if (
            "remember" in prompt_lower
            or "save this" in prompt_lower
            or "store this" in prompt_lower
        ):

            memory = parse_memory(prompt)

            if memory:

                remember(
                    user_id=ctx.author.id,
                    category=memory["category"],
                    key=memory["key"],
                    value=memory["value"]
                )

                return (
                    f"Got it! I'll remember your "
                    f"{memory['key'].replace('_', ' ')}."
                )

            return "I couldn't understand what to remember."

        # ----------------------------
        # RECALL
        # ----------------------------

        elif (
            "what's my favorite" in prompt_lower
            or "what is my favorite" in prompt_lower
        ):

            match = re.search(
                r"favorite (.+)",
                prompt_lower
            )

            if not match:
                return "I couldn't understand what you wanted to recall."

            thing = (
                match.group(1)
                .replace("?", "")
                .replace(".", "")
                .replace("!", "")
                .strip()
            )

            key = f"favorite_{thing.replace(' ', '_')}"

            value = recall(
                ctx.author.id,
                key
            )

            if value:
                return f"Your favorite {thing} is {value}."

            return f"I don't know your favorite {thing} yet."

        # ----------------------------
        # FORGET
        # ----------------------------

        elif "forget my favorite" in prompt_lower:

            match = re.search(
                r"forget my favorite (.+)",
                prompt_lower
            )

            if not match:
                return "I couldn't understand what memory to forget."

            thing = (
                match.group(1)
                .replace("?", "")
                .replace(".", "")
                .replace("!", "")
                .strip()
            )

            key = f"favorite_{thing.replace(' ', '_')}"

            forget(
                ctx.author.id,
                key
            )

            return f"Done! I forgot your favorite {thing}."

        return "I couldn't understand the memory request."

    # --------------------------------------------------
    # Tools
    # --------------------------------------------------

    elif intent == Intent.TOOL:

        result = handle_tool(prompt)

        if result is not None:
            return result

        return "No suitable tool found."

    # --------------------------------------------------
    # Moderation
    # --------------------------------------------------

    elif intent == Intent.MODERATION:

        answer = await discord_handle(ctx, prompt)

        if answer is not None:
            return answer

        return "I couldn't determine the moderation action."

    # --------------------------------------------------
    # Default AI Chat
    # --------------------------------------------------

    else:

        context = build_context(ctx)

        return ask_ai(
            context,
            prompt
        )