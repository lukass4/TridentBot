import discord
from discord import client
from discord.ext import commands
from bot import comingSoon, embedMaker

class rockPaperScissors(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] rockPaperScissors cog has been loaded.") # prints the cog has started

    @commands.command()
    async def rps(self, ctx):
        message = await ctx.send("React with rock paper or scissors!")
        await message.add_reaction(":rock:")
        await message.add_reaction(":newspaper:")
        await message.add_reaction(":scissors:")
        with open("data\\rps_message.txt") as f:
            f.seek(0)
            f.write(str(message))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        pass


def setup(client):
    client.add_cog(rockPaperScissors(client))