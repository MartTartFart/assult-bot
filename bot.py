import discord
import asyncio
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event  

async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
#async = it tells python this function will do some things that takes time, so dont block the whole program, (asynchronous) do this while doing other things too dont block the whole ts program
#ctx = an object that holds information about how and where a command was called (context)
#await = wait until this task is finished before moving onto the next line of code ts

async def assult(ctx, user: discord.Member,*,message='assulted'):
    if ctx.author.guild_permissions.administrator:
        for i in range(40):
            await ctx.send(f"{user.mention} {message}")
    else:
        await ctx.send(f"{ctx.author.mention} you do not have perms lil nga")
  # Wait for 1 second before sending the next message
@bot.command()
async def nuke(ctx,message):
    if ctx.author.guild_permissions.administrator:
        for i in range(15):
            await ctx.send(f"@everyone  {message}")
            asyncio.sleep(2)
    else:
        await ctx.send(f"{ctx.author.mention} you do not have perms lil nga")

@bot.command()
async def ezra(ctx):
    await ctx.send(file=discord.File("ezrah.png"))

@bot.command()
async def Jdog(ctx):
    await ctx.send(file=discord.File("j-dog.png"))

@bot.command()
async def ethan(ctx):
    await ctx.send(file=discord.File("ethan.gif"))
    



bot.run('MTM3MjAxMDA3MjIwODgzNDYxMA.GyhP48.Pf6nCb7DFmGLnOcaupF5kfZqlaPk91_-1dVZwc')