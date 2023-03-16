import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from time import sleep
import ffmpeg
from download_wav import *
import random
load_dotenv()

TOKEN = os.getenv('Token') ##reset token discord developer portal
GUILD = os.getenv('GuildName') ##server name

intents = discord.Intents.default()

intents.members = True
intents.message_content = True
bot=commands.Bot(command_prefix='!', intents=intents) 




@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name='play', help='Plays a song')
async def play(ctx,song_name):
    search_for_song(song_name)
    filename="song.wav"
    server = ctx.message.guild
    channel = server.voice_client
    async with ctx.typing():
        channel.play(discord.FFmpegPCMAudio(executable='/usr/bin/ffmpeg', source=filename))
    await ctx.send('**Now playing:** {}'.format(song_name))

@bot.command(name='leave', help='Tells the bot to leave the voice channel')
async def leave(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        server = ctx.message.guild
        voice_client = server.voice_client
        await voice_client.disconnect()
@bot.command(name='pause', help='Tells the bot to pause the song')
async def pause(ctx):
    channel = ctx.message.guild.voice_client
    channel.pause()

@bot.command(name='resume', help='Tells the bot to resume the song')
async def resume(ctx):
    channel = ctx.message.guild.voice_client
    channel.resume()

@bot.command(name='stop', help='Tells the bot to stop the song')
async def stop(ctx):
    channel = ctx.message.guild.voice_client
    channel.stop()

@bot.command(name='getmemberids', help='Lists all the members in the server')
async def memberids(ctx):
    for member in ctx.guild.members:
        res = "id :"+str(member.id)+" Member Name: "+str(member.name)
        await ctx.send(res)

@bot.command(name='disconnect', help='Kicks a member from the server')
async def move_to(ctx, member: discord.Member, *, reason=None):  
    await member.move_to(None, reason=reason)
    
@bot.command(name='channels', help='Lists all the channels in the server')
async def channels(ctx):
    for channel in ctx.guild.channels:
        res = "Channel Id: "+str(channel.id)+" Channel Name: "+str(channel.name)
        await ctx.send(res)
    

@bot.command(name='voicechannels', help='Lists all the voice channels in the server')
async def voicechannels(ctx):
    for channel in ctx.guild.voice_channels:
        res = "Voice Channel Id: "+str(channel.id)+" Voice Channel Name: ",str(channel.name)
        await ctx.send(res)

def random_voice_channel(ctx):
    voice_channels = ctx.guild.voice_channels
    return random.choice(voice_channels)

@bot.command(name='fuckhim', help='Moves a member to a random voice channel')
async def move_to(ctx, member: discord.Member, *, reason=None):
    global i 
    i =True
    while True:
        if i == False:
            break
        else:
            await member.move_to(random_voice_channel(ctx=ctx), reason=reason)

@bot.command(name='apologize', help='Apogolize for stop moving the member')
async def apologize(ctx,apologize):
    global i
    if apologize == "pardon":
        i = False
        await ctx.send("Good boy...")
    
@bot.command(name='spam', help='Spams a member')
async def spam(ctx, member: discord.Member, *, reason=None):
    for i in range(100):
        user = member
        await user.send("Hello there!") #obiwan kenobi 

@bot.command(name='help', help='Lists all the commands')
async def helpme(ctx):
    await ctx.send("join, play, leave, pause, resume, stop, lol, memberids, disconnect, channels, voicechannels, moverandom, apologize, spam, help")

@bot.command(name='clear', help='Clears the chat')
async def clear(ctx):
    await ctx.channel.purge()

bot.run(TOKEN)
