import discord
from discord import client
from discord.ext import commands
from bot import embedMaker

class rockPaperScissors(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] rockPaperScissors cog has been loaded.") # prints the cog has started

    @commands.command()
    async def rps(self, ctx): # rock paper scissors command
        await ctx.send(embed=embedMaker("Command not available", "This command is coming soon!", discord.Color.blue())) # command error

def setup(client):
    client.add_cog(rockPaperScissors(client))