import discord
from discord import client
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from bot import embedMaker, comingSoon
import json
import math

class suggestions(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] suggestions cog has been loaded.") # prints the cog has started

    @commands.command(aliases=["suggestion", "createsuggestion"])
    @commands.cooldown(1, 300, BucketType.user) # 5 minute user cooldown
    async def suggest(self, ctx, *, suggestion=None):
        if suggestion:
            guild = str(ctx.message.guild.id) # gets the guild ID and makes it into a string
            data = json.load(open("data/suggestion_channels.json", "r")) # loads the json
            try: # checks if there is a suggestion channel set
                channel_id = data[guild][0]
                try: # check if the suggestion channel exists
                    channel = self.client.get_channel(channel_id)
                    message = await channel.send(embed=embedMaker(f"Suggestion by {ctx.author}", f"{suggestion}", discord.Color.blue()))
                    await ctx.send(embed=embedMaker(f"Suggestion Submitted", f"Your suggestion has been submitted in <#{channel_id}>.", discord.Color.blue()))
                    await message.add_reaction("👍")
                    await message.add_reaction("🤷‍♂️")
                    await message.add_reaction("👎")
                except AttributeError:
                    await ctx.send(embed=embedMaker("Suggestion channel not found.", "The channel for suggestions could not found.\nPlease contact a server admin and ask them to set the channel again.", discord.Color.blue()))
                    ctx.command.reset_cooldown(ctx)
            except KeyError:
                await ctx.send(embed=embedMaker("Suggestion channel not found.", "The channel for suggestions has not been setup.\nPlease contact a server admin and ask them to set a suggestions channel.", discord.Color.blue()))
                ctx.command.reset_cooldown(ctx)
        else:
            await ctx.send(embed=embedMaker("Suggestion blank", "Please suggest something. ", discord.Color.blue()))
            ctx.command.reset_cooldown(ctx)

    @commands.command(aliases=["suggestchannel", "setsuggestionchannel", "setsuggestchannel", "setsuggestion", "setsuggest", "suggestionconfig"])
    @commands.has_permissions(administrator=True)
    async def suggestionchannel(self, ctx, channel:discord.TextChannel=None ):
        data = json.load(open("data/suggestion_channels.json", "r"))
        guild = str(ctx.message.guild.id)
        if channel != None:
            try:
                data[guild][0] = int(channel.id)
            except KeyError:
                data[guild] = [[]]
                data[guild][0] = int(channel.id)
            await ctx.send(embed=embedMaker("Suggestion channel set", f"The suggestion channel has been set to <#{channel.id}>", discord.Color.blue()))
        else:
            await ctx.send(embed=embedMaker("Suggestion channel", f"<#{channel.id}>", discord.Color.blue()))

        json.dump(data, open("data/suggestion_channels.json", "w"))

    @suggestionchannel.error
    async def suggestionchannelerror(self, ctx, error):
        if isinstance(error, commands.ChannelNotFound):
            await ctx.send(embed=embedMaker("Suggestion Channel could not be set", f"Please specify a proper channel.\nFor example `,suggestionchannel <channel>`.\nYou can use a channel id or just mention the channel.", discord.Color.blue()))
            


def setup(client):
    client.add_cog(suggestions(client))