# bot.py
import asyncio
import os
import random
import time
import discord
import imageSearchHelper

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
#note, this doesn't actually work, since I forgot that bots ignore other bots
#still useful example of pulling from files and formatting the text inside of them
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
    await ctx.send('set timer for ' + str(seconds) + ' seconds')
    for i in range(seconds):
        await asyncio.sleep(1)

    await ctx.send('timer for ' + str(seconds) + ' seconds is up!')

@bot.command(name='coinflip', help='heads or tails? spits one out randomly')
async def coinflip(ctx):
    rand = random.random()
    if rand < .5:
        await ctx.send('heads!')
    elif (rand > .99):
        await ctx.send('wow you\'re lucky, want a cookie or something, also tails btw')
    else:
        await ctx.send('tails')

@bot.command(name='image', help='Finds first image from google based on input keyword(s)')
async def imageSearch(ctx, *, searchTerm):
    await ctx.send('Pulling image from Google')
    #pulling image using the google-image-search repo
    #listKeywords = " ".join(searchTerm)
    #random * as param seems to be discords way of handling multiple words
    imageSearchHelper.findImage(searchTerm, num=1)
    fileList = os.listdir('downloads')
    #checking if list is empty or not

    
    count = 1
    #pile-driving over common errors
    while not fileList and count < 10:
        count += 1
        imageSearchHelper.findImage(searchTerm, num=count)
        fileList = os.listdir('downloads')
    totalCount = count + 10
    #checking file size, limit of 8 MB for discord
    fileName = 'downloads/' + fileList[0]
    fileSize = os.stat(fileName).st_size
    while fileSize >= 8*1024*1024 and count < totalCount:
        count += 1
        #take out old image
        os.remove(fileName)
        imageSearchHelper.findCountedImage(searchTerm, num=count, randNum=count - 1)
        fileList = os.listdir('downloads')
        if fileList:
            fileName = 'downloads/' + fileList[0]
        else:
            count += 1

    # if (fileSize >= 8*1024*1024):
    #     count += 1
    #     start = count
    #     os.remove(fileName)
    #     #fileList = []

    #     #assume file name is the same from initial call, shouldn't change in a few seconds
    #     imageSearchHelper.findImage(searchTerm, num=count)
    #     os.remove(fileName)
    #     fileList = os.listdir('downloads')
    #     #resetting file Name stuff
    #     fileName = 'downloads/' + fileList[0]
    
    print(fileName)
 

    #sending and removing image
    await ctx.send(file=discord.File(fileName))
    os.remove(fileName)

@bot.command(name='randimage', help='Finds random image from google based on input keyword(s)')
async def randImageSearch(ctx, *, searchTerm):
    await ctx.send('Pulling image from Google')
    randomNum = random.randint(2, 26)
    #pulling image using the google-image-search repo
    #listKeywords = " ".join(searchTerm)
    #random * as param seems to be discords way of handling multiple words
    imageSearchHelper.findCountedImage(searchTerm, num=randomNum, randNum=randomNum - 1)
    fileList = os.listdir('downloads')
    #checking if list is empty or not
    
    count = 1
    while not fileList and count < 10:
        count += 1
        imageSearchHelper.findCountedImage(searchTerm, num=randomNum + count, randNum=randomNum + count - 1)
        fileList = os.listdir('downloads')
    print(fileList[0])
    fileName = 'downloads/' + fileList[0]


    totalCount = count + 10
    #checking file size, limit of 8 MB for discord
    fileName = 'downloads/' + fileList[0]
    fileSize = os.stat(fileName).st_size
    #looping through again
    while fileSize >= 8*1024*1024 and count < totalCount:
        count += 1
        #take out old image
        os.remove(fileName)
        imageSearchHelper.findCountedImage(searchTerm, num=randomNum + count, randNum=randomNum + count - 1)
        fileList = os.listdir('downloads')
        #similar check to first while loop, sometimes images just don't come through
        if fileList:
            fileName = 'downloads/' + fileList[0]
        else:
            count += 1

    #sending and removing image
    await ctx.send(file=discord.File(fileName))
    os.remove(fileName)

@bot.command(name='hello', help='introduction of bob the bot')
async def introduction(ctx):
    await ctx.send(file=discord.File('bot/saitama.jpg'))
    await ctx.send('Hi! My name is bob, and I can do a bunch of random things!')
    await ctx.send('Try out !help to get a list of my commands, and have fun!')


bot.run(TOKEN)