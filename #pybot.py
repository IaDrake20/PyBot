#pybot made by Ian Drake
#from imaplib
#from cgi import print_form
#from urllib import request
import discord
#import requests
#import youtube_dl
import os
from asyncio import tasks
#from codeop import CommandCompiler
from discord.ext import tasks, commands
#from bs4 import BeautifulSoup
#from dotenv import load_dotenv

#client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True
#bot = commands.Bot(command_prefix='$', status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Trying to make MEE6 get a lobotomy", intents = intents))
bot = commands.Bot(command_prefix= '! ', help_command=commands.DefaultHelpCommand(), intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))  


#Respond to new member
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    await bot.process_commands(member)
    
@bot.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send('Testing 1 2 3')
    await bot.process_commands(message)
    
@bot.command()
async def echo(ctx, channel:discord.TextChannel, title, *, message):
    await channel.send("**{}**\n{}".format(title, message))

#scrape first results from google search for image of what user wants        
#@client.event
#async def on_mesage(message):       
#    if message.content.startswith('$Find '):
#        def getdata(url):
#            r = request.get(url)
#            return r.text
#        htmldata = getdata("https://www.google.com/search?q=")#add string or whatuser wants from $Find
#        soup = BeautifulSoup(htmldata, 'html.parser')
#        for item in soup.find_all('img'):
#            print(item['src'])
            
#@client.event
#message should contain $Schedule, (channel_id), (daily/weekly), (hour), (message)
#async def scheduler(message):
#    if message.content.startswith('$Schedule'):
#        seperated_message = message.rsplit(",",4)
#        #set channel_id frm message
#        target_channel_id = seperated_message[1]
#        
#        if seperated_message[2] != 'daily' | target_channel_id != 'weekly':
#            #set default to weekly so its not spammed everyday
#            seperated_message[2] = 'weekly'
            
        
        #set message to daily or weekly
#        time_dw = seperated_message[2]
        
        #set message to send at specified hour
#        time_h = seperated_message[3] 
        
        #messge to be sent
#        msg = seperated_message[4]
        
        #below is what is causing the ifs to have issues
        #@tasks.loop(hours= time_h)
        
#        if "day" in time_dw:
            #async def called_once_a_day():#async
#                message_channel = bot.get_channel(target_channel_id)
#                print(f"Got channel {message_channel}")
                #await message_channel.send(msg)
#        if "week" in time_dw:
            #async def called_once_a_week():
 #               message_channel = bot.get_channel(target_channel_id)
#                print(f"Got channel {message_channel}")
                #await message_channel.send(msg)
#    print("Confirmed")

@bot.command() # This is the decorator we use to create a prefixed command.
async def ping(ctx): # This is the function we will use to create the command.
    await ctx.send("Pong!") # This is the response the bot will send.

    
@bot.command()
async def help_list(message):
    if message.content.startsWith('Help'):
        print("$Hello.\n$Schedule (channel_id), (daily OR weekly), (hour), (message).\n$Schedule (daily OR weekly), (hour), (message).\n$Find (type desired image")
        

bot.run('')