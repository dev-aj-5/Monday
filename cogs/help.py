import discord

from discord.ext import commands

from Data.help_data import HELP_DATA
from version import VERSION


class Help(commands.Cog):

    def __init__(self, bot):

        self.bot = bot


    @commands.command(name="help")

    async def help(self, ctx, category=None):

        if category is None:

            home = HELP_DATA["home"]

            embed = discord.Embed(

                title=home["title"],

                description=home["description"],

                color=discord.Color.blurple()
            )

            for section in home["categories"]:

                data = HELP_DATA[section]

                embed.add_field(

                    name=f'{data["emoji"]} {data["title"]}',

                    value=f'`!help {section}`',

                    inline=False
                )

            embed.set_footer(

                text=f"Monday • v{VERSION}"
            )

            await ctx.send(embed=embed)

            return

        category = category.lower()

        if category not in HELP_DATA:

            embed = discord.Embed(

                title="❌ Unknown Category",

                description=(
                    "Available categories:\n\n"
                    "• ai\n"
                    "• moderation\n"
                    "• memory\n"
                    "• analytics\n"
                    "• tools\n"
                    "• general"
                ),

                color=discord.Color.red()
            )

            await ctx.send(embed=embed)

            return

        data = HELP_DATA[category]

        embed = discord.Embed(

            title=f'{data["emoji"]} {data["title"]}',

            color=discord.Color.blurple()
        )

        for command, description in data["commands"]:

            embed.add_field(

                name=command,

                value=description,

                inline=False
            )

        embed.set_footer(

            text=f"Monday • v{VERSION}"
        )

        await ctx.send(embed=embed)


async def setup(bot):

    await bot.add_cog(

        Help(bot)
    )