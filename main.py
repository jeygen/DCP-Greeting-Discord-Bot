import os
import discord
import requests
import json


client = discord.Client() #connection to discord

TOKEN = os.environ['TOKEN'] 

def get_quote(): #helper func to return from api

@client.event #register event, async library, callback functions activate when something else happens
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$Hello'):
    await message.channel.send('Hi fren!')
    
client.run(TOKEN)