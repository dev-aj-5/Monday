from utils.member_resolver import get_target_member

from services.warning_service import (
    warn,
    get_warnings,
    clear_warnings
)

from utils.moderation_checks import can_moderate


async def handle(ctx, prompt):

    prompt_lower = prompt.lower()

    member = get_target_member(ctx, prompt)

    if member is None:
        return None

    # ==================================================
    # Clear Warnings
    # ==================================================

    if prompt_lower.startswith("clear warnings"):

        error = can_moderate(
            ctx,
            member,
            "moderate_members"
        )

        if error:
            return error

        clear_warnings(
            ctx.guild.id,
            member.id
        )

        return (
            f"✅ Cleared all warnings for "
            f"**{member.display_name}**."
        )
    
    # ==================================================
    # Show Warnings
    # ==================================================

    if (
        prompt_lower.startswith("show warnings") or
        prompt_lower.startswith("warnings")
    ):

        rows = get_warnings(
            ctx.guild.id,
            member.id
        )

        if not rows:
            return f"✅ **{member.display_name}** has no warnings."

        reply = f"⚠️ **Warnings for {member.display_name}**\n\n"

        for i, (reason, date) in enumerate(rows, start=1):

            reply += (
                f"**{i}.** {reason}\n"
                f"📅 {date}\n\n"
            )

        return reply
    
    # ==================================================
    # Warn
    # ==================================================

    if (
    prompt_lower.startswith("warn ")
    or prompt_lower == "warn"
):

        error = can_moderate(
            ctx,
            member,
            "moderate_members"
        )

        if error:
            return error

        reason = prompt.split(member.display_name, 1)[-1].strip()

        if not reason:
            reason = "No reason provided."

        warn(
            ctx.guild.id,
            member.id,
            ctx.author.id,
            reason
        )

        total = len(
            get_warnings(
                ctx.guild.id,
                member.id
            )
        )

        return (
            f"⚠️ Warned **{member.display_name}**.\n"
            f"They now have **{total}** warning(s)."
        )


    return None