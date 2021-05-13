# bot.py
import asyncio
import os
import random
import time

from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

playlistLoaded = False
#songList = []

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='bob', help='standard testing with bob')
async def testResponse(ctx):
    response = 'bob'
    await ctx.send(response)
#add functionality, add songs, remove songs, can try to make it approximate the search?
#maybe play from a range, i.e. song number 1-10.

@bot.command(name='load', help='load a playlist to then use, name must be exact, text file: bob.txt, command, !load bob')
async def loadplaylist(ctx, name):
    playlistName = "bot/" + name + ".txt"
    print(playlistName)
    playlistFile = open(playlistName,'r+')
    #loading playlist into a list of strings
    global songList
    songList = playlistFile.readlines()
    random.shuffle(songList)
    print('loaded')


    playlistFile.close()
    response = 'playlist ready for commands, play, add, delete'
    await ctx.send(response)

@bot.command(name='play', help='plays songs from loaded list, !play #num of songs')
async def playSongs(ctx, numSongs: int):
    random.shuffle(songList)
    for i in range(numSongs):
        response = "-play " + songList[i]
        await ctx.send(response)
        #time.sleep(1)

@bot.command(name='timer', help='creates a timer, put in time as a parameter')
async def makeTimer(ctx, seconds: int):
    for i in range(seconds):
        await asyncio.sleep(1)

    await ctx.send('time is up!')

@bot.command(name='coinflip', help='heads or tails? spits one out randomly')
async def coinflip(ctx):
    rand = random.random()
    if rand < .5:
        await ctx.send('heads!')
    elif (rand > .99):
        await ctx.send('howd you break a coin stupid')
    else:
        await ctx.send('tails')

bot.run(TOKEN)