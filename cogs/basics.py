import discord
from discord.ext import commands
import random
import pandas as pd
from datetime import datetime

class Basics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong {round(self.bot.latency * 1000)}ms')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def scan(self, ctx):
        date = datetime.strptime('Oct 1 2021 12:00AM', '%b %d %Y %I:%M%p')
        data = pd.DataFrame(columns=['content', 'time', 'author'])
        msglimit = 10000

        def is_mention(msg):
            if msg.mentions:
                if msg.author.bot:
                    return True
                else:
                    return False
            else:
                return True

        async for msg in ctx.channel.history(limit=None, after=date):
            if not is_mention(msg) and "<@" in msg.content:
                data = data.append({'content': msg.content,
                                        'time': msg.created_at,
                                        'author': msg.author.id}, ignore_index=True)
                print(data)
        
        file_location = "data.csv"
        data.to_csv(file_location)

    @commands.command()
    async def whisper(self, ctx, user: discord.Member, *, message):
        responses = [
            "Isn't it sad to send a message to yourself?",
            "Are you okay buddy?",
            "Do you need someone to talk to?",
            "Why u want to send message to yourself?"
        ]
        if ctx.author == user:
            await ctx.channel.purge(limit=1)
            return await ctx.author.send(random.choice(responses))
        await user.send(message)
        await ctx.author.send(f'Your message to {user} is sent!')
        await ctx.channel.purge(limit=2)

def setup(bot):
    bot.add_cog(Basics(bot))
