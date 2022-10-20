#pybot made by Ian Drake

#from imaplib
from cgi import print_form
import discord
import requests
import youtube_dl
import os
from asyncio import tasks
from codeop import CommandCompiler
from discord.ext import tasks, commands
from bs4 import BeautifulSoup
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot("$")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  

#Respond to greeting
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#        
@client.event
async def on_mesage(message):       
    if message.content.startswith('$Find '):
        def getdata(url):
            r = requests.get(url)
            return r.text
        htmldata = getdata("https://www.google.com/search?q=")#add string or whatuser wants from $Find
        soup = BeautifulSoup(htmldata, 'html.parser')
        for item in soup.find_all('img'):
            print(item['src'])
            
@client.event
#message should contain $Schedule, (channel_id), (daily/weekly), (hour), (message)
async def scheduler(message):
    if message.content.startswith('$Schedule'):
        seperated_message = message.rsplit(",",4)
        #set channel_id frm message
        channel_id = seperated_message[1]
        
        #set message to daily or weekly
        time_dw = seperated_message[2]
        
        #set message to send at specified hour
        time_h = seperated_message[3] 
        
        #messge to be sent
        msg = seperated_message[4]
        
@client.event
#message should contain $Schedule, (daily/weekly), (hour), (message)
async def scheduler(message):
    
    target_channel_id = 0000
    
    if message.content.startswith('$Schedule'):
        seperated_message = message.rsplit(",",3)
        
        #set message to daily or weekly
        time_dw = seperated_message[1]
        
        #set message to send at specified hour
        time_h = seperated_message[2] 
        
        #messge to be sent
        msg = seperated_message[3] 
        
        @tasks.loop(hours= time_h)
        if "day" in time_dw:
            async def called_once_a_day():
            message_channel = bot.get_channel(target_channel_id)
            print(f"Got channel {message_channel}")
            await message_channel.send(msg)
            
            

client.run('MTAzMjM5ODc3MzE4MTIyNzAwOA.GS_z-I.ga5jGNrDJDcDM-_cwDgpth-5wYqxlP7ic39_9o')