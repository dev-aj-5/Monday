from collections import Counter
from email.mime import message
from services.ai_service import ask_ai

async def handle(ctx, prompt: str):

    prompt = prompt.lower()

    # -----------------------------------
    # Most Active Members
    # -----------------------------------

    if (
        "most active" in prompt
        or "who talked the most" in prompt
        or "most messages" in prompt
        or "who sent the most messages" in prompt
        or "who talks the most" in prompt
    ):

        counter = Counter()

        async for message in ctx.channel.history(limit=500):

            if message.author.bot:
                continue

            counter[message.author.display_name] += 1

        if not counter:
            return "No recent messages found."

        top = counter.most_common(5)

        reply = "📊 **Most Active Members (Last 500 Messages)**\n\n"

        for i, (name, count) in enumerate(top, start=1):

            reply += f"**{i}.** {name} — {count} messages\n"

        return reply
    
    # -----------------------------------
    # Summarize Chat
    # -----------------------------------

    if (
        "summarize" in prompt
        or "summary" in prompt
    ):

        messages = []

        async for message in ctx.channel.history(limit=100):

            if message.author.bot:
                continue

            messages.append(
                f"{message.author.display_name}: {message.content}"
            )

        messages.reverse()

        conversation = "\n".join(messages)

        ai_prompt = f"""
    Summarize the following Discord conversation.

    Keep it concise.

    Mention:
    - Main topics
    - Important decisions
    - Action items

    Conversation:

    {conversation}
"""

        return ask_ai("", ai_prompt)
    
        # -----------------------------------
    # Pinned Messages
    # -----------------------------------

    if (
        "pinned" in prompt
        or "pins" in prompt
    ):

        pins = await ctx.channel.pins()

        if not pins:
            return "There are no pinned messages."

        reply = f"📌 **Pinned Messages ({len(pins)})**\n\n"

        for i, message in enumerate(pins[:5], start=1):
            if message.content:
                content = message.content
            elif message.embeds:
                embed = message.embeds[0]
                content = embed.title or ""
                if embed.description:
                    content += f"\n{embed.description}"
            elif message.attachments:
                content = f"📎 {len(message.attachments)} attachment(s)"
            else:
                content = "[Empty message]"

            if len(content) > 100:
                content = content[:100] + "..."

            reply += (
                f"**{i}.** {message.author.display_name}\n"
                f"{content}\n\n"
            )

        return reply
    
    return None