import os
import discord

# Connection to discord
client = discord.Client() 

# Lists of targeted words/phrases
hellos = ["hi", "hello", "sup", "wazzup", "suh", "holla", "howdy", "yo", "good afternoon"]
goodbyes = ["goodbye", "bye", "later", "goodnight", "till next time", "ta ta", "cya"]

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content in hellos:
    embed = discord.Embed(title="DCP Worker", 
    url="https://dcp.work/?bankAccount=0x72af1bB78185BB3cCba53dBEdC75FEE875434155", #Change this address to earn credits into your own wallet
    description="Hi fren! This link allocates your unused CPU to be used by the distributed compute protocol. Change the address to earn credits to your account! Why not contribute to a super computer while chatting??", color=0xFF5733)
    await message.channel.send(embed=embed)

  if message.content in goodbyes:
    embed = discord.Embed(title="DCP Worker", 
    url = "https://dcp.work/?bankAccount=0x72af1bB78185BB3cCba53dBEdC75FEE875434155", 
    description="Goodbye fren! This link allocates your unused CPU to be used by the distributed compute protocol. Change the address to earn credits to your account! Why not contribute to a super computer while you're not chatting??", color=0xFF5733)
    await message.channel.send(embed=embed)
  
# Token Business    
TOKEN = os.environ['TOKEN']     
client.run(TOKEN)