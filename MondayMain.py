import discord
from discord.ext import commands
import asyncio
from services.logger import info
from config import DISCORD_TOKEN
from services.warning_service import initialize as initialize_warnings
from services.guild_service import (
    initialize as initialize_guilds
)
from services.logger import info
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

from services.guild_service import create_guild


@bot.event
async def on_guild_join(guild):

    create_guild(guild.id)

    info(f"Joined {guild.name}")


@bot.event
async def on_ready():
    info(f"Logged in as {bot.user}")

@bot.event
async def on_command(ctx):
    info(
        f"{ctx.author} executed {ctx.message.content} in #{ctx.channel}"
    )

async def main():
    async with bot:
        info("Loading General Cog...")
        await bot.load_extension("cogs.general")
        await bot.load_extension("cogs.moderation")
        await bot.load_extension("cogs.ai")
        info("General Cog loaded, Moderation Cog oaded, Ai Cog loaded.")
        from services.memory_service import initialize
        initialize()
        initialize_guilds()
        initialize_warnings()
        await bot.start(DISCORD_TOKEN)


asyncio.run(main())

