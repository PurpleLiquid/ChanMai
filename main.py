import discord
from identifier import MaidChan # The bot's identity
from ChatBot import *

client = discord.Client()

myBot = MaidChan()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(activity=discord.Game(name="Serving"))

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        response = chatbot_response(message.content)
        await message.channel.send(response)

client.run(myBot.TOKEN)