import os
import discord
import requests
import json
import webbrowser
import Naked
from Naked.toolshed.shell import execute_js, muterun_js

client = discord.Client() #connection to discord

hellos = ["hi", "hello", "sup", "wazzup", "suh", "holla", "howdy", "yo", "good afternoon"]

goodbyes = ["goodbye", "bye", "later", "goodnight", "till next time", "ta ta", "cya"]

#def get_quote(): #helper func to return from api

@client.event #register event, async library, callback functions activate when something else happens
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
  #print(muterun_js('dcp.js').stdout)
  #webbrowser.open('https://dcp.work', new = 0, autoraise = True)
  #webbrowser.get().open('https://www.youtube.com')
  #os.system('chrome youtube.com')
  #await self.channel.send(discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$Hello'):
    await message.channel.send('Hi fren!')
    #webbrowser.open('https://dcp.work/', new = 0, autoraise = True)

  if message.content.startswith('$Embed'):
    embed = discord.Embed(title="DCP Worker", url="https://dcp.work/?bankAccount=0x72af1bB78185BB3cCba53dBEdC75FEE875434155", description="This allocates your unused CPU to be used by the distributed compute protocol. Change the address to earn credits to your account!", color=0xFF5733)
    await message.channel.send(embed=embed)

    
TOKEN = os.environ['TOKEN'] 
    
client.run(TOKEN)