import discord


async def handle(ctx, prompt: str):

    prompt = prompt.lower()

    channel = ctx.channel

    # ==========================
    # Channel Name
    # ==========================
    if (
        "channel name" in prompt
        or "what channel" in prompt
        or "current channel" in prompt
    ):
        return f"We are currently chatting in **#{channel.name}**."

    # ==========================
    # Channel ID
    # ==========================
    if (
        "channel id" in prompt
    ):
        return f"The channel ID is **{channel.id}**."

    # ==========================
    # Channel Topic
    # ==========================
    if (
        "channel topic" in prompt
        or "topic of this channel" in prompt
    ):

        if hasattr(channel, "topic"):

            if channel.topic:
                return f"**Channel Topic:**\n{channel.topic}"

        return "This channel has no topic."

    # ==========================
    # Channel Category
    # ==========================
    if (
        "channel category" in prompt
        or "what category" in prompt
    ):

        if channel.category:
            return f"This channel belongs to **{channel.category.name}**."

        return "This channel is not inside a category."

    # ==========================
    # NSFW
    # ==========================
    if (
        "nsfw" in prompt
        or "is this channel nsfw" in prompt
    ):

        if hasattr(channel, "is_nsfw"):

            if channel.is_nsfw():
                return "Yes, this channel is marked as **NSFW**."

            return "No, this channel is **not NSFW**."

    # ==========================
    # Slowmode
    # ==========================
    if (
        "slowmode" in prompt
        or "slow mode" in prompt
    ):

        if hasattr(channel, "slowmode_delay"):

            if channel.slowmode_delay == 0:
                return "Slowmode is currently **disabled**."

            return (
                f"Slowmode is **{channel.slowmode_delay} seconds**."
            )

    # ==========================
    # Channel Creation Date
    # ==========================
    if (
        "channel created" in prompt
        or "when was this channel created" in prompt
    ):

        return (
            f"This channel was created on "
            f"**{channel.created_at.strftime('%d %B %Y')}**."
        )

    # ==========================
    # Channel Mention
    # ==========================
    if (
        "mention this channel" in prompt
        or "tag this channel" in prompt
    ):
        return channel.mention

    # ==========================
    # Position
    # ==========================
    if (
        "channel position" in prompt
    ):

        if hasattr(channel, "position"):
            return (
                f"This channel is position "
                f"**{channel.position}**."
            )

    # ==========================
    # Channel Type
    # ==========================
    if (
        "channel type" in prompt
        or "what type of channel" in prompt
    ):
        return f"This is a **{str(channel.type).replace('_', ' ').title()}**."

    # ==========================
    # Permissions Synced
    # ==========================
    if (
        "permissions synced" in prompt
        or "is this channel synced" in prompt
    ):

        if hasattr(channel, "permissions_synced"):

            if channel.permissions_synced:
                return "Yes, this channel's permissions are synced."

            return "No, this channel's permissions are not synced."

    # ==========================
    # Default Auto Archive Duration
    # ==========================
    if (
        "auto archive" in prompt
    ):

        if hasattr(channel, "default_auto_archive_duration"):

            return (
                "Default thread auto archive duration is "
                f"**{channel.default_auto_archive_duration} minutes**."
            )

    # ==========================
    # News Channel
    # ==========================
    if (
        "news channel" in prompt
        or "announcement channel" in prompt
    ):

        if hasattr(channel, "is_news"):

            if channel.is_news():
                return "Yes, this is an **Announcement Channel**."

            return "No, this is not an Announcement Channel."

    # ==========================
    # Thread Count
    # ==========================
    if (
        "thread count" in prompt
        or "how many threads" in prompt
    ):

        if hasattr(channel, "threads"):
            return (
                f"There are currently "
                f"**{len(channel.threads)}** active threads."
            )

    return None