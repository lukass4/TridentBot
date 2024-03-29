import discord
from discord.ext import commands
from bot import comingSoon, embedMaker

class utility(commands.Cog):

    def __init__(self, client): # initializing the cog
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self): # when the cog starts
        print("[DEBUG] utility cog has been loaded.") # prints the cog has started

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

    @commands.command(aliases=["usercooldown", "cooldownend", "resetcooldown"])
    @commands.has_permissions()
    async def removecooldown(self, ctx, member:discord.Member = None):
        if not member:
            await ctx.send(embed=embedMaker("Nickname Change", "Please specify a user.", discord.Color.blue()))
        else:
            for command in self.client.commands:
                command.reset_cooldown(ctx)

    @commands.command(aliases=["startpoll"])
    async def poll(self, ctx):
        await ctx.send(comingSoon())


    @commands.command(aliases=["sn", "setnickname"])
    @commands.has_permissions(manage_nicknames=True)
    async def setnick(self, ctx, member : discord.Member = None, *, nickname=None):
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


    @commands.command()
    async def supportserver(self, ctx):
        await ctx.send(embed=embedMaker("", "Feel free to join my support server [here](<https://discord.gg/u3zTPVFEM7>).", discord.Color.blue()))

def setup(client):
    client.add_cog(utility(client))