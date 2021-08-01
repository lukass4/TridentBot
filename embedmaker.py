import discord
from discord.ext import commands
client = commands.Bot(command_prefix = [","])
def make(eTitle, eDesc, eColor):
    embed = discord.Embed(title=eTitle, description=eDesc, color=eColor)
    embed.set_author(name=client.user.display_name, icon_url=client.user.avatar_url)
    return embed