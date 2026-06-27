import discord

from utils.member_resolver import get_target_member


async def handle(ctx, prompt: str):

    prompt = prompt.lower()

    member = get_target_member(ctx, prompt)

    # ==========================
    # Username
    # ==========================
    if "username" in prompt:
        return f"The username is **{member.name}**."

    # ==========================
    # Display Name
    # ==========================
    if (
        "display name" in prompt
        or "nickname" in prompt
        or "nick name" in prompt
    ):
        return f"The display name is **{member.display_name}**."

    # ==========================
    # User ID
    # ==========================
    if (
        "user id" in prompt
        or "user id" in prompt
    ):
        return f"The user ID is **{member.id}**."

    # ==========================
    # Avatar
    # ==========================
    if (
        "avatar" in prompt
        or "profile picture" in prompt
        or "pfp" in prompt
    ):
        return member.display_avatar.url

    # ==========================
    # Mention
    # ==========================
    if (
        "mention" in prompt
        or "tag" in prompt
    ):
        return member.mention

    # ==========================
    # Is Bot
    # ==========================
    if (
        "is bot" in prompt
        or "is a bot" in prompt
    ):
        if member.bot:
            return f"Yes, **{member.display_name}** is a bot."
        else:
            return f"No, **{member.display_name}** is not a bot."

    # ==========================
    # Joined Server
    # ==========================
    if (
        "joined server" in prompt
        or "joined this server" in prompt
        or "when did" in prompt and "join" in prompt
    ):
        return (
            f"**{member.display_name}** joined this server on "
            f"**{member.joined_at.strftime('%d %B %Y')}**."
        )

    # ==========================
    # Account Creation
    # ==========================
    if (
        "account created" in prompt
        or "account creation" in prompt
        
    ):
        return (
            f"**{member.display_name}'s** account was created on "
            f"**{member.created_at.strftime('%d %B %Y')}**."
        )

    # ==========================
    # Highest Role
    # ==========================
    if (
        "highest role" in prompt
        or "top role" in prompt
    ):
        return (
            f"**{member.display_name}'s** highest role is "
            f"{member.top_role.mention}."
        )

    # ==========================
    # Roles
    # ==========================
    if (
        "roles" in prompt
        or "role list" in prompt
    ):

        roles = [role.mention for role in member.roles if role.name != "@everyone"]

        if not roles:
            return f"**{member.display_name}** has no roles."

        return (
            f"**{member.display_name}** has the following roles:\n"
            + ", ".join(roles)
        )

    # ==========================
    # Boosting
    # ==========================
    if (
        "boosting" in prompt
        or "server booster" in prompt
        or "boost the server" in prompt
    ):
        if member.premium_since:
            return (
                f"Yes, **{member.display_name}** has been boosting "
                f"since **{member.premium_since.strftime('%d %B %Y')}**."
            )

        return f"No, **{member.display_name}** is not boosting the server."

    # ==========================
    # Status (Future)
    # ==========================
    if (
        "status" in prompt
        or "online" in prompt
        or "offline" in prompt
    ):
        return (
            "Presence information is not enabled yet. "
            "It will be available in a future update."
        )

    return None