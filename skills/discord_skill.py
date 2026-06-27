from skills.discord.user_skill import handle as user_handle
from skills.discord.server_skill import handle as server_handle
from skills.discord.channel_skill import handle as channel_handle
from skills.discord.bot_skill import handle as bot_handle


async def handle(ctx, prompt: str):

    # ==========================
    # User Skill
    # ==========================
    response = await user_handle(ctx, prompt)

    if response is not None:
        return response

    # ==========================
    # Server Skill
    # ==========================
    response = await server_handle(ctx, prompt)

    if response is not None:
        return response

    # ==========================
    # Channel Skill
    # ==========================
    response = await channel_handle(ctx, prompt)

    if response is not None:
        return response

    # ==========================
    # Bot Skill
    # ==========================
    response = await bot_handle(ctx, prompt)

    if response is not None:
        return response

    # ==========================
    # Nothing handled it
    # ==========================
    return None