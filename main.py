import discord
from discord.channel import TextChannel
from discord.ext import commands
from dotenv import load_dotenv
import random
import pandas as pd

import os

prefix = '..'

client = discord.Client()
bot = commands.Bot(command_prefix=prefix)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server!')

### COGS ###
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@commands.command()
async def scan(self, ctx):
    data = pd.DataFrame(columns=['content', 'time', 'author'])

    def is_command(msg):
        if len(msg.content) == 0:
            return False
        elif msg.content.split()[0] == '_scan':
            return True
        else:
            return False
    
    async for msg in ctx.message.channel.history(limit=10000):
        if msg.author != client.user:
            if not is_command(msg):
                data = data.append({'content': msg.content,
                                    'time': msg.created_at,
                                    'author': msg.author.name}, ignore_index=True)
            
            if len(data) == limit:
                break
    
    file_location = "data.csv"
    data.to_csv(file_location)



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)