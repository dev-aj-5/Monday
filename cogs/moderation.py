import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):

        await ctx.channel.purge(limit=amount + 1)

        embed = discord.Embed(
    title="🧹 Messages Purged",
    description=f"Successfully deleted **{amount}** messages.",
    color=discord.Color.green()
)

        confirmation = await ctx.send(embed=embed)
        await confirmation.delete(delay=3)

        
    @purge.error
    async def purge_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to use this command.")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Usage: !purge <amount>")
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):

        if member == ctx.author:
            return await ctx.send("❌ You cannot kick yourself.")

        if member == self.bot.user:
            return await ctx.send("❌ I can't kick myself.")

        if member == ctx.guild.owner:
            return await ctx.send("❌ You can't kick the server owner.")

        if member.top_role >= ctx.author.top_role:
            return await ctx.send("❌ That member has an equal or higher role than you.")

        if member.top_role >= ctx.guild.me.top_role:
            return await ctx.send("❌ My role is not high enough to kick that member.")

        await member.kick(reason=reason)

        embed = discord.Embed(
            title="👢 Member Kicked",
            color=discord.Color.orange()
        )

        embed.add_field(name="Member", value=member.mention, inline=False)
        embed.add_field(name="Moderator", value=ctx.author.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)

        await ctx.send(embed=embed)
    @kick.error
    async def kick_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to kick members.")

        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("❌ Member not found.")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Usage: !kick @member [reason]")
            
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):

        if member == ctx.author:
            return await ctx.send("❌ You cannot ban yourself.")

        if member == self.bot.user:
            return await ctx.send("❌ I can't ban myself.")

        if member == ctx.guild.owner:
            return await ctx.send("❌ You can't ban the server owner.")

        if member.top_role >= ctx.author.top_role:
            return await ctx.send("❌ That member has an equal or higher role than you.")

        if member.top_role >= ctx.guild.me.top_role:
            return await ctx.send("❌ My role is not high enough to ban that member.")

        await member.ban(reason=reason)

        embed = discord.Embed(
            title="👢 Member Banned",
            color=discord.Color.orange()
        )

        embed.add_field(name="Member", value=member.mention, inline=False)
        embed.add_field(name="Moderator", value=ctx.author.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)

        await ctx.send(embed=embed)





async def setup(bot):
    await bot.add_cog(Moderation(bot))