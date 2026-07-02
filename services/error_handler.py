import traceback
from services.metrics_service import record_error
import discord
from discord.ext import commands

from services.logger import error


async def handle(ctx, exception):

    # Ignore unknown commands
    if isinstance(exception, commands.CommandNotFound):
        return

    # Missing permissions
    if isinstance(exception, commands.MissingPermissions):

        await ctx.send(
            "❌ You don't have permission to use this command."
        )
        return

    # Missing arguments
    if isinstance(exception, commands.MissingRequiredArgument):

        await ctx.send(
            "⚠️ Missing required arguments."
        )
        return

    # Cooldown
    if isinstance(exception, commands.CommandOnCooldown):

        await ctx.send(
            f"⏳ Try again in {exception.retry_after:.1f} seconds."
        )
        return

    # Unexpected error
    record_error()
    
    error(

    f"""
User : {ctx.author}

Guild : {ctx.guild}

Channel : {ctx.channel}

Command : {ctx.message.content}

{traceback.format_exc()}
"""
)

    embed = discord.Embed(

        title="⚠️ Unexpected Error",

        description=(
            "Something went wrong while executing "
            "that command.\n\n"
            "The error has been logged."
        ),

        color=discord.Color.red()
    )

    await ctx.send(embed=embed)