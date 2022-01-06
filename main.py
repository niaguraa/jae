import discord
from discord.channel import TextChannel
from discord.ext import commands
from dotenv import load_dotenv

import os

prefix = '..'

bot = commands.Bot(command_prefix=prefix)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.commands()
async def ping(ctx):
    await ctx.send('pong')

@bot.commands()
async def pong(ctx):
    await ctx.send('ping')

bot.run(TOKEN)