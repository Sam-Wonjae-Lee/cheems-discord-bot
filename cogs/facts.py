import random
import discord
from discord.ext import commands

class Facts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def facts(self, ctx):
      await ctx.message.delete()
      f = open("facts.txt", "r")

      list_of_facts = []

      for line in f:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_facts.append(line_list)

      f.close()

      fact_s = list_of_facts[random.randint(1, len(list_of_facts))]
      fact_s = " ".join(fact_s)
      embed=discord.Embed(title="Facts!", description=f"{fact_s}", color=ctx.author.color)
      embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Facts(client))