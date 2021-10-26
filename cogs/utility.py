import discord
from discord import client
from discord.ext import commands
from bot import embedMaker
import time

class utility(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] utility cog has been loaded.") # prints the cog has started

#    @commands.command()
#    async def help(self, ctx): # help command
#        await ctx.send(embed=embedMaker("Command not available", "This command is coming soon!", discord.Color.blue())) # sends help message

    @commands.command(aliases=["latency", "pong"])
    async def ping(self, ctx): # latency command
        await ctx.send(embed=embedMaker("Ping", f"My ping is {round(self.client.latency * 1000)}ms", discord.Color.blue())) # sends the bots ping in an embed 

    @commands.command(aliases=["purge", "remove"])
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, msgs=None):
        if msgs != None:
            purge = await ctx.channel.purge(limit=int(msgs)+1)
            purge = len(purge)
            purge = purge-1
            if purge == 1:
                plural = ""
            else:
                plural = "s"
            await ctx.send(embed=embedMaker("Message Removal", f"{purge} message{plural} were removed!", discord.Color.blue()), delete_after=3)
        else:
            await ctx.send(embed=embedMaker("Message Removal", "Please specify an amount of messages you wish to remove.", discord.Color.blue()))


    @commands.command(aliases=["sn", "setnickname"])
    async def setnick(self, ctx, member : discord.Member = None, nickname=None):
        if member != None and nickname != None:
            await member.edit(nick=nickname)
            await ctx.send(embed=embedMaker("Nickname Change", f"{member.mention}'s nickname has been set to {nickname}", discord.Color.blue()))
        else:
            await ctx.send(embed=embedMaker("Nickname Change", "Please specify a user and a nickname.", discord.Color.blue()))

    @commands.command(aliases=["profilepicture", "pfp"])
    async def avatar(self, ctx, member : discord.Member = None):
        if discord.Member != None:
            avatar = f"{member.avatar_url}"
            embed = discord.Embed(title=f"{member.display_name}'s Avatar", text=None, color=discord.Color.blue())
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(utility(client))
