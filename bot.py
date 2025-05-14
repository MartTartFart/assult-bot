import discord
import asyncio
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

# Load .env variables (only needed if you're using a .env file locally)
load_dotenv()

# Enable message content intent
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot ready event
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    print("Commands List:\n\t!assault\n\t!nuke\n\t!ezra\n\t!text\n\t!Jdog\n\t!askPackgod")

# !assault command - tag someone 40 times (admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def assault(ctx, user: discord.Member, *, message='assaulted'):
    for i in range(40):
        await ctx.send(f"{user.mention} {message}")
        await asyncio.sleep(1)

@assault.error
async def assault_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, you do NOT have permission to use this command.")

# !nuke command - @everyone spam (admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, *, message='boom type shit'):
    for i in range(15):
        await ctx.send(f"@everyone {message}")
        await asyncio.sleep(1)

@nuke.error
async def nuke_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention}, you do NOT have permission to use this command.")

# !ezra - send image
@bot.command()
async def ezra(ctx):
    await ctx.send(file=discord.File("ezrah.png"))

# !Jdog - send image
@bot.command()
async def Jdog(ctx):
    await ctx.send(file=discord.File("j-dog.jpg"))

# !text - DM a user (admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def text(ctx, user: discord.Member, *, message):
    try:
        await user.send(message)
        await ctx.send(f"✅ Message sent to {user.name}!")
    except discord.Forbidden:
        await ctx.send("❌ I can't send a DM to this user. They might have DMs disabled.")

# !askPackgod - random roast-style 8ball
@bot.command()
async def askPackgod(ctx, *, message):
    if not message.strip():
        await ctx.send("you need to ask a question bru")
    else:
        responses = [
            'yes', 'no', 'nah', 'FUT NO', 'dumbass question, sybau',
            'js kys', '100%', 'ask me some stupid shit like that again I dare you',
            'im gonna assault you for asking that', 'mmmmmaybe',
            'idk bro im packgod'
        ]
        await ctx.send(random.choice(responses))

# Run the bot using your token
bot.run(os.environ['TOKEN'])
