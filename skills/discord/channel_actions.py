import discord
from utils.moderation_checks import has_permission

async def handle(ctx, prompt: str):

    prompt_lower = prompt.lower()

    # -----------------------------------
    # Create Text Channel
    # -----------------------------------

    if prompt_lower.startswith("create text channel"):

        error = has_permission(
    ctx,
    "manage_channels"
)

        if error:
            return error

        if not ctx.guild.me.guild_permissions.manage_channels:
            return "❌ I don't have permission to manage channels."

        name = prompt[19:].strip().replace(" ", "-")

        if not name:
            return "Please provide a channel name."

        channel = await ctx.guild.create_text_channel(name)

        return f"✅ Created text channel {channel.mention}"

    # -----------------------------------
    # Create Voice Channel
    # -----------------------------------

    if prompt_lower.startswith("create voice channel"):

        error = has_permission(
    ctx,
    "manage_channels"
)
        if error:  
            return error

        if not ctx.guild.me.guild_permissions.manage_channels:
            return "❌ I don't have permission to manage channels."

        name = prompt[20:].strip()

        if not name:
            return "Please provide a channel name."

        channel = await ctx.guild.create_voice_channel(name)

        return f"✅ Created voice channel **{channel.name}**"

    # -----------------------------------
    # Lock Channel
    # -----------------------------------

    if prompt_lower.startswith("lock channel"):

        error = has_permission(
    ctx,
    "manage_channels"
)
        if error:  
            return error

        if not ctx.guild.me.guild_permissions.manage_channels:
            return "❌ I don't have permission to manage channels."

        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False

        await ctx.channel.set_permissions(
            ctx.guild.default_role,
            overwrite=overwrite
        )

        return "🔒 Channel locked."

    # -----------------------------------
    # Unlock Channel
    # -----------------------------------

    if prompt_lower.startswith("unlock channel"):

        error = has_permission(
    ctx,
    "manage_channels"
)
        if error:  
            return error

        if not ctx.guild.me.guild_permissions.manage_channels:
            return "❌ I don't have permission to manage channels."

        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = None

        await ctx.channel.set_permissions(
            ctx.guild.default_role,
            overwrite=overwrite
        )

        return "🔓 Channel unlocked."

    return None