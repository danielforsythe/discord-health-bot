import os
import discord
import logging
from discord.ext import commands
from discord.utils import get
# from dotenv import load_dotenv

# Pass token from .env using *arg parameter
# TOKEN = os.getenv("BARCLYDEBOT_TOKEN")
# Manually set bot token
TOKEN = 'NzY4MTU1MzQ4NDAxNjUxNzUz.X48Wag.6u8x41SyFKW1nAGCKA9L7orTcHQ'
# Channel ID
MAIN_CHANNEL = 766659413775482903

# Set command prefix for bot
bot = commands.Bot(command_prefix = '!')

# Get members list from author's voice channel
def get_members(ctx):
    channel = ctx.author.voice.channel
    members = channel.members
    users = []
    for member in members:
        username = '<@' + str(member.id) + '>'
        users.append(username)
    return users

@bot.event
async def on_ready():
    channel = bot.get_channel(MAIN_CHANNEL)
    await channel.send("BarclydeBot is now online!")
    await bot.change_presence(activity=discord.Game(name="Use !help"))

# Tell author's voice channel members to do a set
@bot.command()
async def set(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        users = get_members(ctx)
        await ctx.send(users)
        await ctx.send("%s says do a set damnit!" % ctx.author.name)
    else:
        await ctx.send("You are not connected to a voice channel")

# Tell author's voice channel members to drink some water
@bot.command()
async def hydrate(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        users = get_members(ctx)
        await ctx.send(users)
        await ctx.send("%s says drink some water nerds!" % ctx.author.name)
    else:
        await ctx.send("You are not connected to a voice channel")

# Tell author's voice channel members to stand up and stretch
@bot.command()
async def stretch(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        users = get_members(ctx)
        await ctx.send(users)
        await ctx.send("%s says stand up and stretch your limbs peasants!" % ctx.author.name)
    else:
        await ctx.send("You are not connected to a voice channel")

bot.run(TOKEN)
