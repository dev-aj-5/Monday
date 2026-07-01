def can_moderate(ctx, member, permission):

    """
    Returns:
        None -> moderation is allowed
        str  -> error message
    """

    bot_member = ctx.guild.me

    # ----------------------------
    # User Permission
    # ----------------------------

    if not getattr(ctx.author.guild_permissions, permission):
        return f"❌ You don't have permission to perform this action."

    # ----------------------------
    # Bot Permission
    # ----------------------------

    if not getattr(bot_member.guild_permissions, permission):
        return f"❌ I don't have permission to perform this action."

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
    # Author Hierarchy
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
    
    def has_permission(ctx, permission):

        bot_member = ctx.guild.me

    if not getattr(ctx.author.guild_permissions, permission):
        return "❌ You don't have permission to perform this action."

    if not getattr(bot_member.guild_permissions, permission):
        return "❌ I don't have permission to perform this action."

    return None
