from services.guild_service import set_setting


async def handle(ctx, prompt):

    prompt_lower = prompt.lower()

    if prompt_lower != "set log channel":
        return None

    set_setting(
        ctx.guild.id,
        "log_channel",
        ctx.channel.id
    )

    return (
        f"✅ {ctx.channel.mention} "
        "has been set as the log channel."
    )