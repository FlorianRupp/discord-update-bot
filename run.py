import json
import os
import subprocess

from discord.ext import commands


TOKEN = os.environ["DC_TOKEN"]

bot = commands.Bot(command_prefix='!')

# read config
with open("dc_bot.cfg", "r") as f:
    CONFIG = json.load(f)

channels = [c["channel_id"] for c in CONFIG]


def check_trigger(title):
    for c in CONFIG:
        if title.split(" ")[0] == f"[{c['repo']}:{c['branch']}]".lower():
            return c
    return False


@bot.command(name="botstop")
async def botstop(ctx):
    await ctx.send("Shutdown bot.")
    await bot.close()
    print("Stopped bot.")


@bot.command(name="conf")
async def conf(ctx):
    await ctx.send(CONFIG)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id in channels:
        if len(message.embeds) > 0:
            title = message.embeds[0].title
            result = check_trigger(title)
            if result is not False:
                await message.channel.send(
                    f"Thank you {message.embeds[0].author.name}, I will trigger an update pull on the server.")
                subprocess.Popen(result["script"])

    await bot.process_commands(message)


bot.run(TOKEN)
