import discord

from discord.ext import commands

from version import (
    VERSION,
    BUILD,
    AUTHOR,
    REPOSITORY,
    CODENAME
)

from services.config_service import get
from services.health_service import get_health


class About(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="about",
        aliases=["info"]
    )
    async def about(self, ctx):

        config = get()

        health = get_health(self.bot)

        embed = discord.Embed(

            title="🤖 Monday",

            description=(
                "**An intelligent Discord assistant "
                "that thinks before it speaks.**"
            ),

            color=discord.Color.blurple()
        )

        # -------------------------
        # System
        # -------------------------

        embed.add_field(

            name="📦 Version",

            value=(
                f"**Version:** {VERSION}\n"
                f"**Codename:** {CODENAME}\n"
                f"**Build:** {BUILD}"
            ),

            inline=False
        )

        embed.add_field(

            name="⚙️ Environment",

            value=config["mode"].capitalize(),

            inline=True
        )

        embed.add_field(

            name="👨‍💻 Developer",

            value=AUTHOR,

            inline=True
        )

        # -------------------------
        # Runtime
        # -------------------------

        embed.add_field(

            name="📡 Runtime",

            value=(
                f"**Servers:** {health['servers']}\n"
                f"**Users:** {health['users']}\n"
                f"**Latency:** {health['latency']} ms"
            ),

            inline=False
        )

        # -------------------------
        # AI Providers
        # -------------------------

        providers = "\n".join(
            f"• {provider.title()}"
            for provider in config["providers"]
        )

        embed.add_field(

            name="🧠 AI Providers",

            value=providers,

            inline=False
        )

        # -------------------------
        # GitHub
        # -------------------------

        embed.add_field(

            name="🌐 Repository",

            value=REPOSITORY,

            inline=False
        )

        embed.set_footer(

            text=f"Monday • v{VERSION}"
        )

        if self.bot.user.avatar:

            embed.set_thumbnail(

                url=self.bot.user.avatar.url
            )

        await ctx.send(embed=embed)


async def setup(bot):

    await bot.add_cog(

        About(bot)
    )