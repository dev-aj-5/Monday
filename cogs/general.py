from discord.ext import commands
import discord
import random
from services.logger import info

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(f"{ctx.author.mention} said: {message}")

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"🏓 Pong! `{latency}ms`")

    @commands.command()
    async def roll(self, ctx):
        number = random.randint(1, 6)
        await ctx.send(f"🎲 You rolled a **{number}**!")

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):

        if member is None:
            member = ctx.author

        await ctx.send(member.display_avatar.url)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author

        embed = discord.Embed(
            title=f"👤 {member.display_name}",
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(url=member.display_avatar.url)

        embed.add_field(
            name="Username",
            value=member.name,
            inline=True
        )

        embed.add_field(
            name="Display Name",
            value=member.display_name,
            inline=True
        )

        embed.add_field(
            name="User ID",
            value=member.id,
            inline=False
        )

        embed.add_field(
            name="Account Created",
            value=member.created_at.strftime("%d %B %Y"),
            inline=True
        )

        embed.add_field(
            name="Joined Server",
            value=member.joined_at.strftime("%d %B %Y"),
            inline=True
        )

        embed.set_footer(text=f"Requested by {ctx.author.display_name}")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))

