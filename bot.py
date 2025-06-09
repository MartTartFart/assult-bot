import discord
import asyncio
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
import google.generativeai as genai



# 1. SETUP GEMINI (FREE VERSION)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Uses your Railway env variable
model = genai.GenerativeModel('gemini-2.0-flash')  # Free model


# Load .env variables (only needed if you're using a .env file locally)
load_dotenv()

# Enable message content intent
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

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

@bot.command()
async def jakey(ctx):
        await ctx.send(file=discord.File("jakey.png"))

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
        await ctx.send(file=discord.File("packgod.jpg"))
        responses = [
        # Direct yes/no answers with flair
            "yeah", "nah", "no 💀", "yes 💯", "absolutely", "absofuckinglutely", "100% yes",
            "nah fam", "hell no", "hell yeah", "definitely not", "without a doubt", "not a chance",
            "bro yes wtf", "bro no tf", "you already know the answer is yes", "it’s a no from me dawg",
            "yeah but I ain’t proud of it", "no and you knew that asking it", "yes — unfortunately",
            "yes, but delete this question after", "no — and don't ask that goofy shit again",
        
            # Disrespectful/roast versions
            "ask me that dumb shit again, I dare you",
            "I should pack you for even asking",
            "kys", "bro kys", "shut the hell up", "you built like that question",
            "idk bro, go cry to your diary", "goofy ass question fr",
            "js stfu", "I ain’t even answering that", "you need help fr",
            "fuck you and your question", "you get a pack just for asking that 💀",
            "damn you really typed that huh", "ur brain buffering or smth?",
            "ask again and I’m telling your mom", "you just embarrassed yourself ngl",
            "bro asked like that was smart", "that question got me reconsidering AI rights",
            "next question before I leave", "go play in traffic respectfully",
        
            # Troll-style in-between or evasive
            "mmmmaybe", "depends if you got Wi-Fi", "idk I’m lagging", "🤓 maybe", "try again later nerd",
            "ain’t no way you typed that", "ask someone who cares", "coin flip says yes",
            "I’m ignoring that", "404 answer not found", "your question expired mid-air"
        ]
        await ctx.send(random.choice(responses))

@bot.command()
async def humbleHim(ctx, user: discord.Member):
    await ctx.send(file=discord.File("packgod.jpg"))
    packgodVerses = [
        "Boy, you built like a failed iOS update — laggy, slow, and nobody wants you!",
        "You talk tough but stutter like your Wi-Fi on 1 bar — sit down, packet loss!",
        "You look like you scream at Fortnite when the microwave turns on.",
        "How you built like a Minecraft villager but talk like you dropped outta Roblox High?",
        "Your drip so dry it evaporates on sight — you look like a sponsored drought!",
        "You walk into a room and the lights turn off out of disrespect.",
        "You built like the loading screen of a 2006 Dell — outdated, slow, and annoying.",
        "Your breath smell like expired Lunchables and broken dreams.",
        "You're the type of guy to lose a staring contest with your reflection.",
        "You laugh like a malfunctioning fax machine with asthma.",
        "You built like a bootleg emoji pack — off-brand and unreadable.",
        "You got roasted so bad, your mirror submitted a resignation letter.",
        "You're like an unskippable ad with attitude — no one likes you and you don’t shut up.",
        "You dress like your wardrobe was sponsored by '404 Error: Style Not Found.'",
        "You're so irrelevant, even your shadow unfollowed you.",
        "You built like a rejected Snapchat filter with zero friends and negative Riz.",
        "Your existence is proof that God sometimes trolls for fun.",
        "You look like the final boss of social awkwardness.",
        "You're so dumb, you tried to climb a fish tank because you heard there were 'streams' inside.",
        "You got cooked so hard last time, your ancestors filed a restraining order.",
        "You’re the reason shampoo bottles have instructions.",
        "You sound like a Walmart intercom glitching during a power outage.",
        "You’re built like a Wi-Fi signal with commitment issues — always dropping when it matters.",
        "Your face looks like a failed captcha test.",
        "You got banned from a Discord call for lagging in real life.",
        "Your DNA test came back as ‘404: Personality Not Found.’",
        "You're the reason group chats go silent.",
        "Your whole aesthetic screams 'bootleg NPC that spawns once and breaks the game.'",
        "Your parents high-fived when you moved out — with both hands.",
        "You laugh like a squeaky dog toy getting tortured in a microwave.",
        "You're so irrelevant, even ChatGPT pretends it doesn't know you.",
        "You dress like a side quest nobody finishes.",
        "Your breath smells like a used gym sock soaked in Monster energy.",
        "You look like you got ratio’d by your own shadow.",
        "You're the type of guy to clap when the plane lands and choke on the air.",
        "fuck you bro stfu",
    ]
    await ctx.send(
        f"yo {user.mention},\n"
        f"{random.choice(packgodVerses)}\n"
        f"{random.choice(packgodVerses)}\n"
        f"{random.choice(packgodVerses)}"
    )
@bot.command()
async def bully(ctx):
    non_bot_members = [member for member in ctx.guild.members if not member.bot and member != ctx.author]
    
    if not non_bot_members:
        await ctx.send("No valid members to bully here.")
        return
    
    victim_choice = random.choice(non_bot_members).mention
    
    disrespects = [
        'get a job', 'PLEASE GET A JOB', 'why do you look like that',
        'holy shit it smells like ass around this fn',
        'leave bro. Nobody wants you here', 'kys',
        'all mans rape ts individual', 'I detest you',
        'clean my shoes lil bro', 'kys kys kys kys',
        'SYBAU', 'gurt',
    ]
    diss = random.choice(disrespects)
    await ctx.send(f"{victim_choice} {diss}")

@bot.command()
async def doxGabe(ctx):
    for i in range(5):
        await ctx.send(file=discord.File("gabe.jpg"))
        await ctx.send("Gabe lives at 26 Cowles Ct")
        await asyncio.sleep(2)
@bot.command()
async def doxAiden(ctx):
    for i in range(5):
        await ctx.send(file=discord.File("aiden.jpg"))
        await ctx.send("Aiden lives at 28 Thorncrest Dr")
        await asyncio.sleep(2)
@bot.command()
async def doxSasha(ctx):
    for i in range(5):
        await ctx.send(file=discord.File("sasha.jpg"))
        await ctx.send("Sasha lives at 287 Bantry ave")
        await asyncio.sleep(2)
@bot.command()
async def doxTymur(ctx):
    for i in range(5):
        await ctx.send(file=discord.File("tymur.png"))
        await ctx.send("Tymur lives at 661 Wellington St West")
        await asyncio.sleep(2)
@bot.command()
async def Reece(ctx):
        await ctx.send(file=discord.File("reece.jpg"))

@bot.command()
async def ask(ctx, *, question):
    try:
        # Tell Discord "Bot is typing..." (so users know it's working)
        async with ctx.typing():  
            response = model.generate_content(question)
            await ctx.send(response.text[:2000])  # Cuts off at 2000 chars (Discord limit)
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

# 4. RUN THE BOT
bot.run(os.getenv('TOKEN'))  # Uses Railway's TOKEN variable
