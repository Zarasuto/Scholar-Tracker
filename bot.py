import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f"Ping : {round(client.latency * 1000)}ms ")

for filename in os.listdir('./commands'):
    if(filename.endswith('.py')):
        client.load_extension(f'commands.{filename[:-3]}')

client.run("ODcyMTk4MDY4MjkwODc5NTU4.YQmXwA.q5ckFJLRLRKWIB2EHNkOdLeWDsI")