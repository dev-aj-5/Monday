from skills.discord.user_skill import handle as user_handle
from skills.discord.server_skill import handle as server_handle
from skills.discord.channel_skill import handle as channel_handle
from skills.discord.bot_skill import handle as bot_handle
from skills.discord.analytics import handle as analytics_handle
from skills.discord.actions import handle as actions_handle
from skills.discord.channel_actions import handle as channel_action_handle
from skills.moderation.member import handle as moderation_member_handle
from skills.moderation.warnings import handle as warnings_handle
from skills.setup import handle as setup_handle

async def handle(ctx, prompt: str):

    # ==========================
    # Setup (highest priority)
    # ==========================
    response = await setup_handle(ctx, prompt)

    if response is not None:
        return response

    # ==========================
    # Moderation
    # ==========================
    response = await moderation_member_handle(ctx, prompt)

    if response is not None:
        return response

    # ==========================
    # Warnings
    # ==========================
    response = await warnings_handle(ctx, prompt)

    if response is not None:
        return response

    # ==========================
    # Channel Actions
    # ==========================
    response = await channel_action_handle(ctx, prompt)

    if response is not None:
        return response

    # ==========================
    # General Actions
    # ==========================
    response = await actions_handle(ctx, prompt)

    if response is not None:
        return response

    # ==========================
    # Analytics
    # ==========================
    response = await analytics_handle(ctx, prompt)

    if response is not None:
        return response

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