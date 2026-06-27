from datetime import datetime


def build_context(ctx):

    return f"""
SERVER INFORMATION

Server Name:
{ctx.guild.name}

Channel:
{ctx.channel.name}

User:

Username:
{ctx.author.name}

Display Name:
{ctx.author.display_name}

User ID:
{ctx.author.id}

Current Time:
{datetime.now().strftime("%d %B %Y %H:%M")}
"""