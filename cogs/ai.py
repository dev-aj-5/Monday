from discord.ext import commands
from services.conversation_service import get_recent_messages, format_conversation
from brain.brain import MondayBrain

brain = MondayBrain()


class AI(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ask(self, ctx, *, prompt):

        async with ctx.typing():
            answer = await brain.think(ctx, prompt)

        if len(answer) <= 1900:
            await ctx.send(answer)
        else:
            for i in range(0, len(answer), 1900):
                await ctx.send(answer[i:i+1900])


async def setup(bot):
    await bot.add_cog(AI(bot))