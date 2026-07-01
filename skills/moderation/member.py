import datetime
import discord

from utils.member_resolver import get_target_member
from utils.moderation_checks import can_moderate
from services.logger_service import log


async def handle(ctx, prompt: str):

    prompt_lower = prompt.lower()

    member = get_target_member(ctx, prompt)

    # ==================================================
    # Kick
    # ==================================================

    if prompt_lower.startswith("kick"):

        if member is None:
            return "❌ Member not found."

        error = can_moderate(
            ctx,
            member,
            "kick_members"
        )

        if error:
            return error

        await member.kick(
            reason=f"Requested by {ctx.author}"
        )

        await log(
            ctx.bot,
            ctx.guild.id,
            "👢 Member Kicked",
            (
                f"**Moderator:** {ctx.author.mention}\n"
                f"**Target:** {member.mention}"
            ),
            discord.Color.orange()
        )

        return f"👢 Kicked **{member.display_name}**."

    # ==================================================
    # Ban
    # ==================================================

    if prompt_lower.startswith("ban"):

        if member is None:
            return "❌ Member not found."

        error = can_moderate(
            ctx,
            member,
            "ban_members"
        )

        if error:
            return error

        await member.ban(
            reason=f"Requested by {ctx.author}"
        )

        await log(
            ctx.bot,
            ctx.guild.id,
            "🔨 Member Banned",
            (
                f"**Moderator:** {ctx.author.mention}\n"
                f"**Target:** {member.mention}"
            ),
            discord.Color.red()
        )

        return f"🔨 Banned **{member.display_name}**."

    # ==================================================
    # Timeout
    # ==================================================

    if prompt_lower.startswith("timeout"):

        if member is None:
            return "❌ Member not found."

        error = can_moderate(
            ctx,
            member,
            "moderate_members"
        )

        if error:
            return error

        until = discord.utils.utcnow() + datetime.timedelta(minutes=10)

        await member.timeout(
            until,
            reason=f"Requested by {ctx.author}"
        )

        await log(
            ctx.bot,
            ctx.guild.id,
            "⏳ Member Timed Out",
            (
                f"**Moderator:** {ctx.author.mention}\n"
                f"**Target:** {member.mention}\n"
                f"**Duration:** 10 minutes"
            ),
            discord.Color.gold()
        )

        return f"⏳ Timed out **{member.display_name}** for 10 minutes."

    # ==================================================
    # Unban
    # ==================================================

    if prompt_lower.startswith("unban"):

        error = can_moderate(
            ctx,
            ctx.author,  # permission check only
            "ban_members"
        )

        if error and "yourself" not in error:
            return error

        username = prompt[6:].strip()

        if not username:
            return "Please specify the user's name."

        bans = [entry async for entry in ctx.guild.bans()]

        for ban in bans:

            if (
                ban.user.name.lower() == username.lower()
                or str(ban.user).lower() == username.lower()
            ):

                await ctx.guild.unban(
                    ban.user,
                    reason=f"Requested by {ctx.author}"
                )

                await log(
                    ctx.bot,
                    ctx.guild.id,
                    "✅ Member Unbanned",
                    (
                        f"**Moderator:** {ctx.author.mention}\n"
                        f"**Target:** {ban.user}"
                    ),
                    discord.Color.green()
                )

                return f"✅ Unbanned **{ban.user}**."

        return "❌ That user isn't banned."

    # ==================================================
    # Purge
    # ==================================================

    if prompt_lower.startswith("purge"):

        if not ctx.author.guild_permissions.manage_messages:
            return "❌ You don't have permission to purge messages."

        if not ctx.guild.me.guild_permissions.manage_messages:
            return "❌ I don't have permission to purge messages."

        parts = prompt_lower.split()

        if len(parts) < 2:
            return "Usage: Purge <amount>"

        try:
            amount = int(parts[1])
        except ValueError:
            return "Please provide a valid number."

        if amount < 1 or amount > 100:
            return "Amount must be between 1 and 100."

        deleted = await ctx.channel.purge(limit=amount + 1)

        await log(
            ctx.bot,
            ctx.guild.id,
            "🧹 Messages Purged",
            (
                f"**Moderator:** {ctx.author.mention}\n"
                f"**Deleted:** {len(deleted) - 1} messages"
            ),
            discord.Color.blurple()
        )

        return f"🧹 Deleted {len(deleted) - 1} messages."

    return None