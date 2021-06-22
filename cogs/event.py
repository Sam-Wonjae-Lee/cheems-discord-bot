import discord
import os
from discord.ext import commands, tasks
from discord import Activity, ActivityType

class Event(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.check_rate_limited.start()

    def cog_unload(self):
      self.check_rate_limited.cancel()

    @tasks.loop(seconds=5.0)
    async def check_rate_limited(self):
        #print(self.client.is_ws_ratelimited())
        if self.client.is_ws_ratelimited():
          os.system('kill 1')
        else:
          pass
    
    @tasks.loop(seconds=60.0)
    async def check_servers(self):
      await self.client.change_presence(activity=Activity(
            name=f"{len(self.client.guilds)} Servers | c!help",
            type=ActivityType.watching))

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=Activity(
            name=f"{len(self.client.guilds)} Servers | c!help",
            type=ActivityType.watching))
        print("We have logged in as {0.user}".format(self.client))
        self.check_servers.start()
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.delete()
            em = discord.Embed(title="That's Not A Command!",
                               description="Use c!help To Know The Commands",
                               color=ctx.author.color)
            await ctx.send(embed=em)

          

    



def setup(client):
    client.add_cog(Event(client))
