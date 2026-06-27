import discord


async def get_recent_messages(ctx, limit=20):
    """
    Returns the most recent messages from the current channel.
    """

    messages = []

    async for message in ctx.channel.history(limit=limit):

        # Ignore system messages only
        if message.type != discord.MessageType.default:
            continue

        # Ignore empty messages
        if not message.content.strip():
            continue

        messages.append({
            "author": message.author.display_name,
            "content": message.content,
            "created_at": message.created_at
        })

    messages.reverse()

    return messages


def format_conversation(messages):
    """
    Converts message history into a readable conversation transcript.
    """

    transcript = "Recent Discord Conversation:\n\n"

    for message in messages:

        transcript += (
            f"{message['author']}:\n"
            f"{message['content']}\n\n"
        )

    return transcript.strip()


async def answer_from_history(ctx, question, limit=20):
    """
    Reads recent conversation and answers a question about it.
    """

    messages = await get_recent_messages(ctx, limit)

    conversation = format_conversation(messages)

    prompt = f"""
You are Monday, a Discord assistant.

Below is the recent conversation from the Discord channel.

Answer the user's question ONLY using the conversation below.

If the answer cannot be found in the conversation, clearly say that you couldn't find it.

--------------------------

{conversation}

--------------------------

User Question:

{question}
"""

    from services.ai_service import ask_ai

    return ask_ai("", prompt)