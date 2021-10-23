import discord
from discord import client
from discord.ext import commands
from bot import embedMaker

class maths(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] maths cog has been loaded.") # prints the cog has started

    @commands.command(aliases=["math", "m"])
    async def maths(self, ctx, no1=None, symbol=None, no2=None): # maths command

        if None in (no1, symbol, no2): # checking all arguments have been passed
            await ctx.send("1 or more arguments are incorrect, should be `number symbol number` (example: 2 * 5)") # error message

        else: # if all arguments are specified
            try:
                no1 = int(no1) # checking no1 is actually a number
                no2 = int(no2) # checking no2 is actually a number

                if symbol == "+": # if the symbol is +
                    await ctx.send(embed=embedMaker("Math Output", str(no1 + no2), discord.Color.blue())) # add no1 and no2

                if symbol == "-": # if the symbol is -
                    await ctx.send(embed=embedMaker("Math Output", str(no1 - no2), discord.Color.blue())) # subtract no1 and no2

                if symbol == "*": # if the symbol is *
                    await ctx.send(embed=embedMaker("Math Output", str(no1 * no2), discord.Color.blue())) # multiply no1 and no2 

                if symbol == "/": # if the symbol is /
                    await ctx.send(embed=embedMaker("Math Output", str(no1 / no2), discord.Color.blue())) # divide no1 and no2

                if symbol == "^":
                    await ctx.send(embed=embedMaker("Math Output", str(no1 ** no2), discord.Color.blue()))

            except ValueError: # if no1 or no2 is not a number
                await ctx.send("1 or more arguments are incorrect, should be `number symbol number` (example: 2 * 5)") # error message
            
            
def setup(client):
    client.add_cog(maths(client))