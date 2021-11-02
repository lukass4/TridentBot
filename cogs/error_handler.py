import discord
from discord import client
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from bot import embedMaker, comingSoon
from math import floor

class error_handler(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] error handler cog has been loaded.") # prints the cog has started

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.CommandOnCooldown): # if there is a cooldown
            await ctx.send(embed=embedMaker(f"Command on cooldown", f"That command is on cooldown, retry in {floor(error.retry_after)} seconds.", discord.Color.blue()))
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=embedMaker(f"Missing Permissions", f"You do not have permissions to use this command.\nIf you think you should be able to do this command please join the support server (,supportserver)", discord.Color.blue()))


def setup(client):
    client.add_cog(error_handler(client))