import discord


async def handle(ctx, prompt: str):

    prompt = prompt.lower()
    guild = ctx.guild

    # ==========================
    # Server Name
    # ==========================
    if (
        "server name" in prompt
        or "name of this server" in prompt
    ):
        return f"The server is **{guild.name}**."

    # ==========================
    # Server ID
    # ==========================
    if (
        "server id" in prompt
        or "guild id" in prompt
    ):
        return f"The server ID is **{guild.id}**."

    # ==========================
    # Server Owner
    # ==========================
    if (
        "server owner" in prompt
        or "owner of this server" in prompt
        or "who owns this server" in prompt
):

        owner = ctx.guild.get_member(ctx.guild.owner_id)

        if owner is None:
            owner = await ctx.guild.fetch_member(ctx.guild.owner_id)

        return f"The owner of this server is {owner.display_name}."

    # ==========================
    # Member Count
    # ==========================
    if (
        "member count" in prompt
        or "how many members" in prompt
        or "members in this server" in prompt
    ):
        return f"This server currently has **{guild.member_count}** members."

    # ==========================
    # Creation Date
    # ==========================
    if (
        "server created" in prompt
        or "when was this server created" in prompt
        or "creation date" in prompt
    ):
        return (
            f"**{guild.name}** was created on "
            f"**{guild.created_at.strftime('%d %B %Y')}**."
        )

    # ==========================
    # Verification Level
    # ==========================
    if (
        "verification level" in prompt
        or "server verification" in prompt
    ):
        return (
            f"The server verification level is "
            f"**{guild.verification_level.name.replace('_', ' ').title()}**."
        )

    # ==========================
    # Boost Level
    # ==========================
    if (
        "boost level" in prompt
        or "server boost level" in prompt
    ):
        return f"The server boost level is **Level {guild.premium_tier}**."

    # ==========================
    # Boost Count
    # ==========================
    if (
        "boost count" in prompt
        or "how many boosts" in prompt
        or "server boosts" in prompt
    ):
        return (
            f"The server currently has "
            f"**{guild.premium_subscription_count}** boosts."
        )

    # ==========================
    # Emoji Count
    # ==========================
    if (
        "emoji count" in prompt
        or "how many emojis" in prompt
    ):
        return f"This server has **{len(guild.emojis)}** custom emojis."

    # ==========================
    # Sticker Count
    # ==========================
    if (
        "sticker count" in prompt
        or "how many stickers" in prompt
    ):
        return f"This server has **{len(guild.stickers)}** stickers."

    # ==========================
    # Role Count
    # ==========================
    if (
        "role count" in prompt
        or "how many roles" in prompt
    ):
        return f"This server has **{len(guild.roles)}** roles."

    # ==========================
    # Text Channel Count
    # ==========================
    if (
        "text channels" in prompt
        or "how many text channels" in prompt
    ):
        return (
            f"This server has "
            f"**{len(guild.text_channels)}** text channels."
        )

    # ==========================
    # Voice Channel Count
    # ==========================
    if (
        "voice channels" in prompt
        or "how many voice channels" in prompt
    ):
        return (
            f"This server has "
            f"**{len(guild.voice_channels)}** voice channels."
        )

    # ==========================
    # Categories
    # ==========================
    if (
        "categories" in prompt
        or "how many categories" in prompt
    ):
        return (
            f"This server has "
            f"**{len(guild.categories)}** categories."
        )

    # ==========================
    # AFK Channel
    # ==========================
    if (
        "afk channel" in prompt
    ):
        if guild.afk_channel:
            return f"The AFK channel is **{guild.afk_channel.name}**."

        return "This server doesn't have an AFK channel."

    # ==========================
    # AFK Timeout
    # ==========================
    if (
        "afk timeout" in prompt
    ):
        return (
            f"The AFK timeout is "
            f"**{guild.afk_timeout} seconds**."
        )

    # ==========================
    # Server Description
    # ==========================
    if (
        "server description" in prompt
        or "description of this server" in prompt
    ):
        if guild.description:
            return guild.description

        return "This server has no description."

    # ==========================
    # Server Banner
    # ==========================
    if (
        "server banner" in prompt
    ):
        if guild.banner:
            return guild.banner.url

        return "This server doesn't have a banner."

    # ==========================
    # Server Icon
    # ==========================
    if (
        "server icon" in prompt
        or "server logo" in prompt
    ):
        if guild.icon:
            return guild.icon.url

        return "This server doesn't have an icon."

    return None