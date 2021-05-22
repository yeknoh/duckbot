import discord
from discord.ext import commands
import time
import os
import random
import asyncio
from itertools import cycle
from cfg import *


client = commands.Bot(command_prefix='?')


# number of recently used ducks it should keep track of to not use again
numRecentDucks = 10
# time (in seconds) between ?duck commands
cooldown = 2


recentDucks = []
timeOfLastCommand = 0.0


async def change_status():
    await client.wait_until_ready()
    msg = cycle(status)

    while not client.is_closed():
        current_status = next(msg)
        await client.change_presence(activity=discord.Game(name=current_status))
        await asyncio.sleep(900)


@client.event
async def on_ready():
    print(f"Bot ready, logged in as:", str(client.user.name + '#' + client.user.discriminator))
    print(f"User ID:", client.user.id)
    print(f"Number of ducks: {duckCount}")


# add a statement to block command in direct messages
@client.command()
@commands.has_permissions(administrator=True)
async def loadcog(extension):
    client.load_extension(f'cogs.{extension}')


# add a statement to block command in direct messages
@client.command()
@commands.has_permissions(administrator=True)
async def unloadcog(extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# add a statement to block command in direct messages
@client.command()
@commands.has_permissions(administrator=True)
async def quack(ctx):
    await ctx.send(f'Quacks back after {round(client.latency * 1000)}ms')


@client.command(aliases=['goose', 'farfetchd', 'psyduck'])
async def duck(ctx):
    # cooldown tracking
    global timeOfLastCommand
    if time.time() - timeOfLastCommand < cooldown:
        return

    timeOfLastCommand = time.time()

    path = random.choice(os.listdir(duckpath))
    # if the file is in our recently used, pick another until it isn't
    while path in recentDucks:
        path = random.choice(os.listdir(duckpath))
    # add this new file to the beginning of the list
    recentDucks.insert(0, path)
    # if our list has more than numRecentDucks elements, remove the oldest one
    if len(recentDucks) > numRecentDucks:
        recentDucks.pop()

    await ctx.send(file=discord.File(duckpath + path))

# loop for change status
client.loop.create_task(change_status())

client.run(dtoken)
