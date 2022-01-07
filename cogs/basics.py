import discord
from discord.ext import commands
import random

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
