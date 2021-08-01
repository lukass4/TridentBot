import discord
from discord import client
from discord.ext import commands
from bot import embedMaker

class utility(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] utility cog has been loaded.") # prints the cog has started

    @commands.command()
    async def help(self, ctx): # help command
        await ctx.send(embed=embedMaker("Command not available", "This command is coming soon!", discord.Color.blue())) # sends help message

    @commands.command(aliases=["latency", "pong"])
    async def ping(self, ctx): # latency command
        await ctx.send(embed=embedMaker("Ping", f"My ping is {round(self.client.latency * 1000)}ms", discord.Color.blue())) # sends the bots ping in an embed 

def setup(client):
    client.add_cog(utility(client))