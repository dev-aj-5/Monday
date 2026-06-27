import discord

from config import BOT_NAME, BOT_VERSION


async def handle(ctx, prompt: str):

    prompt = prompt.lower()

    bot = ctx.bot

    # ==========================
    # Bot Name
    # ==========================
    if (
        "your name" in prompt
        or "who are you" in prompt
        or "what is your name" in prompt
    ):
        return f"I'm **{BOT_NAME}**, your Discord assistant."

    # ==========================
    # Bot Version
    # ==========================
    if (
        "version" in prompt
        or "bot version" in prompt
    ):
        return f"I'm currently running **Version {BOT_VERSION}**."

    # ==========================
    # Ping / Latency
    # ==========================
    if (
        "ping" in prompt
        or "latency" in prompt
    ):
        latency = round(bot.latency * 1000)

        return f"My current latency is **{latency} ms**."

    # ==========================
    # Server Count
    # ==========================
    if (
        "how many servers" in prompt
        or "server count" in prompt
    ):
        return f"I'm currently connected to **{len(bot.guilds)}** servers."

    # ==========================
    # User Count
    # ==========================
    if (
        "how many users" in prompt
        or "user count" in prompt
        or "how many people" in prompt
    ):
        users = len(bot.users)

        return f"I can currently see **{users}** Discord users."

    # ==========================
    # Owner
    # ==========================
    if (
        "who created you" in prompt
        or "who made you" in prompt
        or "who is your creator" in prompt
    ):
        return "I was created by **Avi**."

    # ==========================
    # Invite Link
    # ==========================
    if (
        "invite link" in prompt
        or "invite yourself" in prompt
        or "bot invite" in prompt
    ):
        return (
            "I don't have an invite link configured yet."
        )

    # ==========================
    # Current Prefix
    # ==========================
    if (
        "prefix" in prompt
        or "command prefix" in prompt
    ):
        return "My current command prefix is **!**."

    # ==========================
    # AI Provider
    # ==========================
    if (
        "ai provider" in prompt
        or "which ai" in prompt
        or "what ai do you use" in prompt
    ):
        return (
            "I can automatically switch between multiple AI providers "
            "depending on availability."
        )

    # ==========================
    # Current AI Model
    # ==========================
    if (
        "current model" in prompt
        or "which model" in prompt
    ):
        return (
            "The active AI model depends on which provider "
            "is currently available."
        )

    # ==========================
    # Help
    # ==========================
    if (
        "help" == prompt.strip()
        or "what can you do" in prompt
    ):
        return (
            "I can help with:\n\n"
            "• Discord information\n"
            "• User information\n"
            "• Server information\n"
            "• Channel information\n"
            "• AI conversations\n"
            "• Moderation commands"
        )

    return None