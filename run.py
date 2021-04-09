import json
import os
import subprocess

import discord


TOKEN = os.environ["DC_TOKEN"]
client = discord.Client()

# read config
with open("dc_bot.cfg", "r") as f:
    CONFIG = json.load(f)

channels = [c["channel_id"] for c in CONFIG]


def check_trigger(title):
    for c in CONFIG:
        if title.split(" ")[0] == f"[{c['repo']}:{c['branch']}]".lower():
            return c
    return False


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "!botstop" in message.content:
        await client.close()
        print("Stopped bot.")

    if message.channel.id in channels:
        if len(message.embeds) > 0:
            title = message.embeds[0].title
            result = check_trigger(title)
            if result is not False:
                await message.channel.send(
                    f"Thank you {message.embeds[0].author.name}, I will trigger an update pull on the server.")
                subprocess.Popen(result["script"])


client.run(TOKEN)
