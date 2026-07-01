import discord

from services.guild_service import get_setting


async def log(
    bot,
    guild_id,
    title,
    description,
    color=discord.Color.blurple()
):
    channel_id = get_setting(
        guild_id,
        "log_channel"
    )

    if channel_id is None:
        return

    guild = bot.get_guild(guild_id)

    if guild is None:
        return

    channel = guild.get_channel(channel_id)

    if channel is None:
        return

    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    await channel.send(embed=embed)