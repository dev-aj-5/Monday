import discord


async def handle(ctx, prompt: str):

    prompt_lower = prompt.lower()

    if "create poll" not in prompt_lower:
        return None

    lines = prompt.splitlines()

    if len(lines) < 3:
        return (
            "Usage:\n"
            "!ask Create poll\n"
            "Question\n"
            "Option 1\n"
            "Option 2\n"
            "Option 3"
        )

    question = lines[1]

    options = lines[2:12]

    numbers = [
        "1️⃣",
        "2️⃣",
        "3️⃣",
        "4️⃣",
        "5️⃣",
        "6️⃣",
        "7️⃣",
        "8️⃣",
        "9️⃣",
        "🔟"
    ]

    description = ""

    for emoji, option in zip(numbers, options):
        description += f"{emoji} {option}\n"

    embed = discord.Embed(
        title="📊 Poll",
        description=question,
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="Options",
        value=description,
        inline=False
    )

    poll = await ctx.send(embed=embed)

    for emoji in numbers[:len(options)]:
        await poll.add_reaction(emoji)

    return "Poll created successfully."