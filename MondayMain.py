import discord
from discord.ext import commands
import asyncio
from utils.logger import logger
from config import DISCORD_TOKEN


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)


@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user}")

@bot.event
async def on_command(ctx):
    logger.info(
        f"{ctx.author} executed {ctx.message.content} in #{ctx.channel}"
    )

async def main():
    async with bot:
        logger.info("Loading General Cog...")
        await bot.load_extension("cogs.general")
        await bot.load_extension("cogs.moderation")
        await bot.load_extension("cogs.ai")
        logger.info("General Cog loaded, Moderation Cog oaded, Ai Cog loaded.")
        await bot.start(DISCORD_TOKEN)


asyncio.run(main())
