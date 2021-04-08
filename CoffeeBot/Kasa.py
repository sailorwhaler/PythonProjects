import asyncio, os, discord
from kasa import Discover, SmartPlug
from discord.ext import commands
from dotenv import load_dotenv
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


#Load Discord server info
load_dotenv()
token = os.getenv('DiscordToken')
GUILD = os.getenv('DiscordGuild')
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    

#Discover Kasa plug
device = asyncio.run(Discover.discover())
for addr, dev in device.items():
    asyncio.run(dev.update())

#Update plug
plug = SmartPlug(addr)
asyncio.run(plug.update())

bot.run(token)
