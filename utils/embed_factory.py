import discord

from version import VERSION


def create_embed(title, description=None, color=discord.Color.blurple()):

    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )

    embed.set_footer(
        text=f"Monday • v{VERSION}"
    )

    return embed
