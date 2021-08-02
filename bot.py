import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = [","]) # creating bot variable with prefixes
client.remove_command("help") # remove default help command

eColor = discord.Color.blue()

@client.event
async def on_ready(): # when bot starts
    print(f"[DEBUG] {client.user} has started") # prints the bot has started
    await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name="your commands")) # changing the bots status


def embedMaker(eTitle, eDesc, eColor): # embed maker function
    embed = discord.Embed(title=eTitle, description=eDesc, color=eColor) # does title, description and colour
    embed.set_author(name=client.user.display_name, icon_url=client.user.avatar_url) # sets the name and profile picture to the bots
    return embed

def comingSoon(): # embed maker function
    embed = discord.Embed(title="Command not available", description="This command is coming soon!", color=eColor) # does title, description and colour
    embed.set_author(name=client.user.display_name, icon_url=client.user.avatar_url) # sets the name and profile picture to the bots
    return embed


for filename in os.listdir("./cogs"): # loading cogs
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}") # loads the cog without the .py on the end

client.run("ODcwMjIzOTQyODM1NjUwNTYx.YQJpMw.xxM5gzu-0oRaRjnK-4jQ-otjUBE") # running with the token

