import os
import discord

# Get secrets from environment variables.

# Bot token from https://discord.com/developers/applications.
TOKEN = os.environ['TOKEN']
# DCP Bank Account Address. e.g., 0x72af1bB78185BB3cCba53dBEdC75FEE875434155
# Change this address to earn credits into your own wallet.
BANK_ACCOUNT = os.environ['BANK_ACCOUNT']

# URL that the embedded message links to.
embed_url = f"https://dcp.work/?bankAccount={BANK_ACCOUNT}"

# Connection to discord
client = discord.Client() 

# Lists of targeted words/phrases
hellos = ["hi", "Hi", "hello", "Hello", "sup", "wazzup", "suh", "holla", "howdy", "yo", "good afternoon"]
goodbyes = ["goodbye", "Goodbye", "bye", "Bye", "later", "goodnight", "till next time", "ta ta", "cya"]

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content in hellos:
    message_prefix = "Hi"
  elif message.content in goodbyes:
    message_prefix = "Goodbye"

  embed = discord.Embed(title="DCP Worker", 
    url = embed_url,
    description=f"{message_prefix} fren! This link allocates your unused CPU to be used by the distributed compute protocol. Change the address to earn credits to your account! Why not contribute to a super computer while you're not chatting??", color=0xFF5733)

  await message.channel.send(embed=embed)


client.run(TOKEN)