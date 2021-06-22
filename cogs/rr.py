import discord
from discord.ext import commands
import random
import asyncio

class RussianRoulette(commands.Cog):
    def __init__(self, client):
        self.client = client

    global i
    i = 0

    @commands.command()
    async def rr(self, ctx):
      await ctx.message.delete()
      user = ctx.message.author.mention
      global i
      chance = 6 - i
      num = random.randint(1, chance)

      if i == 0:
        embed=discord.Embed(description="Reloads Revolver...", color=ctx.author.color)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        embed=discord.Embed(description="Spins Chamber...", color=ctx.author.color)
        await ctx.send(embed=embed)
      else:
        embed=discord.Embed(description="Already Loaded...", color=ctx.author.color)
        await ctx.send(embed=embed)

      await asyncio.sleep(2)
      embed=discord.Embed(description="Pulls Trigger...", color=ctx.author.color)
      await ctx.send(embed=embed)
      await asyncio.sleep(2)

      if num == 1:
        embed=discord.Embed(description="Revolver Fires!  🔥🔫", color=16711680)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        embed=discord.Embed(description="You Died " + user + "! ⚰️", color=16711680)
        await ctx.send(embed=embed)
        i = 0
      else:
       embed=discord.Embed(description="Revolver Clicks!  🔫", color=65280)
       await ctx.send(embed=embed)
       await asyncio.sleep(2)
       embed=discord.Embed(description="You Survived " + user + "! 😀", color=65280)
       await ctx.send(embed=embed)
       i += 1

def setup(client):
    client.add_cog(RussianRoulette(client))