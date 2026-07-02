from discord.ext import commands
import discord
from services.metrics_service import get_metrics
from services.health_service import get_health

metrics = get_metrics()

class Health(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def health(self, ctx):

        health = get_health(self.bot)

        embed = discord.Embed(

            title="🩺 Monday Health",

            color=discord.Color.green()
        )

        embed.add_field(
            name="Version",
            value=health["version"],
            inline=True
        )

        embed.add_field(
            name="Build",
            value=health["build"],
            inline=True
        )

        embed.add_field(
            name="Uptime",
            value=health["uptime"],
            inline=True
        )

        embed.add_field(
            name="Servers",
            value=health["servers"],
            inline=True
        )

        embed.add_field(
            name="Users",
            value=health["users"],
            inline=True
        )

        embed.add_field(
            name="Latency",
            value=f'{health["latency"]} ms',
            inline=True
        )

        embed.add_field(
            name="Memory Database",
            value="✅ Online" if health["database"] else "❌ Offline",
            inline=False
        )

        providers = "\n".join(
            f"✅ {p}"
            for p in health["providers"]
        )

        embed.add_field(
            name="AI Providers",
            value=providers,
            inline=False
        )

        embed.add_field(
            name="Commands Executed",
            value=metrics["commands"],
            inline=True
        )

        embed.add_field(
            name="Errors",
            value=metrics["errors"],
            inline=True
        )

        embed.add_field(
            name="AI Requests",
            value=metrics["ai_requests"],
            inline=True
        )

        await ctx.send(embed=embed)


async def setup(bot):

    await bot.add_cog(
        Health(bot)
    )