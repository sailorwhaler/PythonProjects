import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='~', intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord server!'
    )

@bot.command(name='owo')
async def owo(ctx):
    owo_gifs = [
        'https://tenor.com/view/egoz-uwu-uwu-army-dance-party-gif-15090789',
        'https://tenor.com/view/uwu-smug-anime-stare-gif-17603924',
        'https://tenor.com/view/discord-uwu-sweat-blush-gif-13566033',
        'https://tenor.com/view/uw-u-kawai-pixel-art-gif-18479273'

    ]
    response = random.choice(owo_gifs)
    await ctx.send(response)
    await ctx.message.delete()

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name="real-python"):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command')



@bot.command(name='uwuify')
async def uwuify(ctx):
    messageID = ctx.message.reference.message_id
    message = await ctx.channel.fetch_message(messageID)
    newMessage = message.content #I'm a string
    newMessage = newMessage.replace("r", "w")
    newMessage = newMessage.replace("l", 'w')
    await ctx.send("UwU" + message.author.mention + " " + newMessage)
    await ctx.message.delete()

bot.run(TOKEN)