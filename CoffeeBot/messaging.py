import asyncio, os, discord
from threading import Timer
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



#Discover Kasa plug
device = asyncio.run(Discover.discover())
for addr, dev in device.items():
    asyncio.run(dev.update())

#Update plug
plug = SmartPlug(addr)
asyncio.run(plug.update())
#print(plug.is_on)

def timeryeet():
    asyncio.run(TimerHandler())

@bot.event
async def TimerHandler():
    print('timer triggered')   
    user = bot.get_user(249956665347145728)
    print(user)
    if plug.is_on == True:
        await user.create_dm()
        await user.dm_channel.send(
            f'Good morning {user.display_name}'
    )

    
t = Timer(5.0, timeryeet)
t.start()

bot.run(token)