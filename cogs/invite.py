import discord
from discord.ext import commands

from version import (
    VERSION,
    REPOSITORY
)
from utils.embed_factory import create_embed

# --------------------------------------------------
# CHANGE THIS LATER
# --------------------------------------------------

BOT_INVITE = "https://discord.com/oauth2/authorize?client_id=1519243684145533020&permissions=8&integration_type=0&scope=bot+applications.commands"

SUPPORT_SERVER = "Coming Soon"

DOCUMENTATION = REPOSITORY


class Invite(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()

    async def invite(self, ctx):

        embed = create_embed(

            title="📨 Invite Monday",

            description=(
                "Thanks for your interest in Monday!\n\n"
                "Use the links below to invite the bot "
                "or learn more."
            ),

            color=discord.Color.blurple()
        )

        embed.add_field(

            name="🤖 Invite",

            value=BOT_INVITE,

            inline=False
        )

        embed.add_field(

            name="📚 Documentation",

            value=DOCUMENTATION,

            inline=False
        )

        embed.add_field(

            name="💻 GitHub",

            value=REPOSITORY,

            inline=False
        )

        embed.add_field(

            name="💬 Support Server",

            value=SUPPORT_SERVER,

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

        Invite(bot)
    )