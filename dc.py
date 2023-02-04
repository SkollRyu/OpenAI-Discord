# This example requires the 'message_content' intent.

import discord
from OpenAI import ask_question

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        question = message.content.split(" ", 1)[1]
        completion = ask_question(question)
        answer = completion["choices"][0]["text"]
        await message.channel.send(answer)

client.run('MTA2OTk2MjE4MjA0NzA0NzcxMA.GZUoER.sD9eKx5I9RSkKEn-1rxSELgeES1-fncNmsqiNU')
