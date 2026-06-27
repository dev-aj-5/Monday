import discord


def get_target_member(ctx, prompt: str = "") -> discord.Member:
    """
    Returns the member the user is referring to.

    Priority:
    1. Mentioned member
    2. Username
    3. Display name (nickname)
    4. Command author
    """

    # ----------------------------
    # Mention
    # ----------------------------
    if ctx.message.mentions:
        return ctx.message.mentions[0]

    prompt = prompt.lower()

    # ----------------------------
    # Username / Nickname Search
    # ----------------------------
    for member in ctx.guild.members:

        if member.name.lower() in prompt:
            return member

        if member.display_name.lower() in prompt:
            return member

    # ----------------------------
    # Default
    # ----------------------------
    return ctx.author