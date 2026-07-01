def has_permission(ctx, permission):

    bot_member = ctx.guild.me

    # ----------------------------
    # User Permission
    # ----------------------------

    if not getattr(ctx.author.guild_permissions, permission):
        return "❌ You don't have permission to perform this action."

    # ----------------------------
    # Bot Permission
    # ----------------------------

    if not getattr(bot_member.guild_permissions, permission):
        return "❌ I don't have permission to perform this action."

    return None


def can_moderate(ctx, member, permission):

    error = has_permission(ctx, permission)

    if error:
        return error

    bot_member = ctx.guild.me

    # ----------------------------
    # Self
    # ----------------------------

    if member == ctx.author:
        return "❌ You can't moderate yourself."

    # ----------------------------
    # Server Owner
    # ----------------------------

    if member == ctx.guild.owner:
        return "❌ The server owner cannot be moderated."

    # ----------------------------
    # User Hierarchy
    # ----------------------------

    if (
        member.top_role >= ctx.author.top_role
        and ctx.author != ctx.guild.owner
    ):
        return (
            "❌ You can't moderate someone with an equal "
            "or higher role than you."
        )

    # ----------------------------
    # Bot Hierarchy
    # ----------------------------

    if member.top_role >= bot_member.top_role:
        return (
            "❌ I can't moderate someone with an equal "
            "or higher role than mine."
        )

    return None