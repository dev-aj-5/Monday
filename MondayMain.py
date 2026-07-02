import asyncio

import discord
from discord.ext import commands
from config import DISCORD_PREFIX
from config import DISCORD_TOKEN, MODE
from version import VERSION, CODENAME

from services.logger import info

from services.startup import (
    banner,
    check_environment,
    initialize_services,
    finish
)

from services.guild_service import (
    initialize as initialize_guilds,
    create_guild
)

from services.warning_service import (
    initialize as initialize_warnings
)

from services.memory_service import (
    initialize as initialize_memory
)

from services.error_handler import handle as handle_error
# ==================================================
# Discord Intents
# ==================================================

intents = discord.Intents.default()
intents.message_content = True

# ==================================================
# Bot
# ==================================================

bot = commands.Bot(
    command_prefix=DISCORD_PREFIX,
    intents=intents,
    help_command=None
)

# Prevent duplicate on_ready() execution
_ready = False

# ==================================================
# Events
# ==================================================

@bot.event
async def on_ready():

    global _ready

    if _ready:
        return

    _ready = True

    finish()

    total_users = sum(g.member_count or 0 for g in bot.guilds)

    info("=" * 45)
    info(f"Connected As : {bot.user}")
    info(f"Version      : {VERSION} ({CODENAME})")
    info(f"Mode         : {MODE}")
    info(f"Servers      : {len(bot.guilds)}")
    info(f"Users        : {total_users}")
    info(f"Latency      : {round(bot.latency * 1000)} ms")
    info("=" * 45)


@bot.event
async def on_guild_join(guild):

    create_guild(guild.id)

    info(f"Joined server: {guild.name}")


@bot.event
async def on_command(ctx):

    info(
        f"{ctx.author} executed "
        f"{ctx.message.content} "
        f"in #{ctx.channel}"
    )
    from services.metrics_service import record_command
    record_command(ctx.command.name)


@bot.event
async def on_command_error(ctx, exception):

    await handle_error(
        ctx,
        exception
    )
# ==================================================
# Startup Helpers
# ==================================================

async def load_cogs():

    cogs = [
        "cogs.general",
        "cogs.moderation",
        "cogs.ai",
        "cogs.health"
    ]

    info("Loading Cogs...")

    for cog in cogs:

        await bot.load_extension(cog)

        info(f"✓ {cog.split('.')[-1].capitalize()}")
        

    info("All cogs loaded successfully.")


def initialize_databases():

    info("Initializing Services...")

    initialize_memory()
    info("✓ Memory")

    initialize_guilds()
    info("✓ Guild Settings")

    initialize_warnings()
    info("✓ Warnings")

    info("Services initialized successfully.")

# ==================================================
# Main
# ==================================================

async def main():

    banner()

    check_environment()

    initialize_services()

    initialize_databases()

    async with bot:

        await load_cogs()

        await bot.start(DISCORD_TOKEN)

# ==================================================
# Launch
# ==================================================

if __name__ == "__main__":
    asyncio.run(main())