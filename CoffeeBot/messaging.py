import asyncio, os, discord
from kasa import Discover, SmartPlug
from discord.ext import commands, tasks
from dotenv import load_dotenv
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)


#Load Discord server info
load_dotenv()
token = os.getenv('DiscordToken')
GUILD = os.getenv('DiscordGuild')


#Discover Kasa plug
#device = asyncio.run(Discover.discover())
#addr = ""
#for addr, dev in device.items():
    #asyncio.run(dev.update())
    #print(f'addr = {addr} dev = {dev}')
    
#Update plug
plug = SmartPlug("192.168.1.4")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected ')
    TimerHandler.start()


@tasks.loop(minutes=2)
async def TimerHandler():
    print('timer triggered')   
    user = bot.get_user(249956665347145728)
    print(user)
    
    await plug.update()
    
    if plug.is_on == True:
        print('plug is on')
        await user.create_dm()
        await user.dm_channel.send(
            f'Good morning {user.display_name}'
    )
    else:
        print('plug is off')


bot.run(token)
