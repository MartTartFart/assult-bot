import discord
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load .env variables (only needed if you're using a .env file locally)
load_dotenv()

# Enable message content intent
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot startup message
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# !assult command - tag someone 40 times (admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def assult(ctx, user: discord.Member, *, message='assulted'):
    for i in range(40):
        await ctx.send(f"{user.mention} {message}")
        await asyncio.sleep(1)  # Wait 1 second between messages

# !nuke command - @everyone spam (admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, *, message):
    for i in range(15):
        await ctx.send(f"@everyone {message}")
        await asyncio.sleep(2)  # You forgot to "await" before asyncio.sleep()

# Image commands
@bot.command()
async def ezra(ctx):
    await ctx.send(file=discord.File("ezrah.png"))

@bot.command()
async def Jdog(ctx):
    await ctx.send(file=discord.File("j-dog.jpg"))  # You wrote .png but posted .jpg

@bot.command()
async def ethan(ctx):
    await ctx.send(file=discord.File("ethan.gif"))

# Start the bot using the token from .env or environment variable
bot.run(os.environ['TOKEN'])
