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

# Bot startup message
@bot.event
async def help():
    print(f"Commands List:\n\t!assult\n\t!nuke\n\t!ezra\n\t!text\n\t!Jdog")
    
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# !assult command - tag someone 40 times (admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def assault(ctx, user: discord.Member, *, message='assaulted'):
        for i in range(40):
            await ctx.send(f"{user.mention} {message}")
            await asyncio.sleep(1)  # Wait 1 second between messages
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{user.mention} you do NOT have perms lil bro pack it up")
    # Do something, like send a message to the user


# !nuke command - @everyone spam (admin only)
@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, *, message='boom type shit'):
    for i in range(15):
        await ctx.send(f"@everyone {message}")
        await asyncio.sleep(1)  # You forgot to "await" before asyncio.sleep()
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{user.mention} you do NOT have perms lil bro pack it up")
# Image commands
@bot.command()
async def ezra(ctx):
    await ctx.send(file=discord.File("ezrah.png"))

@bot.command()
async def Jdog(ctx):
    await ctx.send(file=discord.File("j-dog.jpg"))  # You wrote .png but posted .jpg
@bot.command()
@commands.has_permissions(administrator=True)
async def text(ctx, user: discord.Member, *, message):
    try:
        await user.send(message)
        await ctx.send(f"✅ Message sent to {user.name}!")
    except discord.Forbidden:
        await ctx.send("❌ I can't send a DM to this user. They might have DMs disabled.")

@bot.command()
async def askPackgod(ctx,message):
    if not message:
        await ctx.send("you need to ask a question bru")
    else:
        responses = ['yes','no','nah','FUT NO','dumbass question, sybau','js kys','100%','ask me some supid shit like that again I dare you','im gonna assult you for asking that', 'yes','no','mmmmmaybe','idk bro im packgod']
        await ctx.send(random.choice(responses))
    
# Start the bot using the token from .env or environment variable
bot.run(os.environ['TOKEN'])
