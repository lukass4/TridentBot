import discord
from discord import client
from discord.ext import commands
from bot import embedMaker, comingSoon
import random

class fun(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] fun cog has been loaded.") # prints the cog has started

    @commands.command()
    async def boop(self, ctx, member : discord.Member=None):
        if member == None:
            await ctx.send("Please specify a member you wish to boop.")
        else:
            try:
                await member.send(embed=embedMaker("Boop!", f"You have been booped by {ctx.author}.", discord.Color.blue()))
                await ctx.send(embed=embedMaker("Booped!", f"{member} has been booped successfully.", discord.Color.blue()))
            except:
                await ctx.send(embed=embedMaker("Not Booped. :frowning2:", f"{member} has not been booped successfully. I cannot message them.", discord.Color.blue()))

    @commands.command(aliases=["coinflip", "cf", "flip"])
    async def coin(self, ctx):
        if random.choice([1, 2]) == 1:
            await ctx.send(embed=embedMaker("Coin Flip :coin:", "Heads! ", discord.Color.blue()))
        else:
            await ctx.send(embed=embedMaker("Coin Flip :coin:", "Tails!", discord.Color.blue()))


def setup(client):
    client.add_cog(fun(client))