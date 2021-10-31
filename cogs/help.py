import discord
from bot import client
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from bot import embedMaker, comingSoon, debug
from math import floor

class help(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] help cog has been loaded.") # prints the cog has started

    @commands.command()
    async def help(self, ctx, category=None):
        if not category:           
            embed = discord.Embed(title="Help Command", description="Here are a list of the modules you can query for help.", color=discord.Colour.blue()) # does title, description and colour
            embed.add_field(name="Fun Commands", value="`,help fun`", inline=True)
            embed.add_field(name="Math Commands", value="`,help math`", inline=True)
            embed.add_field(name="Utility Commands", value="`,help utility`", inline=True)
            embed.add_field(name="Suggestions Commands", value="`,help suggestions`", inline=True)
            embed.add_field(name="Moderation Commands", value="`,help moderation`", inline=True)
            debug("help command ran")
            await ctx.send(embed=embed)

        elif category == "fun":
            embed = discord.Embed(title="Fun Help", description="Here are a list of the fun commands", color=discord.Colour.blue())
            embed.add_field(name=",boop <@user>", value="Sends a message to the user saying \"boop!\"", inline=False)
            embed.add_field(name=",coinflip", value="It's in the name, flips a coin.", inline=False)
            embed.set_footer(text="Use `,help` to see all modules")
            await ctx.send(embed=embed)
            
        elif category == "math":
            embed = discord.Embed(title="Math Help", description="Here are a list of the math commands", color=discord.Colour.blue())
            embed.add_field(name=",math <no1> <operation> <no2>", value="Use `+`,`-`,`*`,`/` in the operations to do basic math.", inline=False)
            embed.set_footer(text="Use `,help` to see all modules")
            await ctx.send(embed=embed)

        elif category == "utility":
            embed = discord.Embed(title="Utility Help", description="Here are a list of the utility commands", color=discord.Colour.blue())
            embed.add_field(name=",purge <no of messages>", value="Clears a number of messages", inline=False)
            embed.add_field(name=",setnick <@user>", value="Sets a users nickname", inline=False)
            embed.add_field(name=",avatar <@user>", value="Fetches a users profile picture", inline=False)
            embed.set_footer(text="Use `,help` to see all modules")
            await ctx.send(embed=embed)

        elif category == "suggestions":
            embed = discord.Embed(title="Suggestions Help", description="Here are a list of the suggestions commands", color=discord.Colour.blue())
            embed.add_field(name=",suggest <suggestion>", value="Sends a message to a set suggestion channel", inline=False)
            embed.add_field(name=",suggestionchannel", value="Sets a suggestion channel for the suggestion messages", inline=False)
            embed.set_footer(text="Use `,help` to see all modules")
            await ctx.send(embed=embed)

        elif category == "moderation":
            await ctx.send(comingSoon())

        else:
            await ctx.send(embed=embedMaker("Error", "That is not a valid help command, use `,help` to see all modules.", discord.Color.blue()))

def setup(client):
    client.add_cog(help(client))