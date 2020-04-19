import discord
from identifier import MaidChan # The bot's identity

client = discord.Client()
myBot = MaidChan()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="Serving"))


client.run(myBot.TOKEN)