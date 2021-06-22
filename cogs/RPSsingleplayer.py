import discord
from discord.ext import commands
import random
import asyncio

class RPS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rps(self, ctx):
      await ctx.message.delete()
      buttons=["🪨", "🧾", "✂️"]
      embed=discord.Embed(title="Rock Paper Scissors!", description="Choose `Rock`, `Paper` Or `Scissors` For Your Answer!", color=ctx.author.color)
      embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
      sent=await ctx.send(embed=embed)

      for button in buttons:
         await sent.add_reaction(button)

      while True:
        try:
            reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)

        except asyncio.TimeoutError:
            await sent.delete()
            break

        else:
          bot_rps="rps"
          rps_random=random.choice(bot_rps)
          
          if rps_random == "r":
            if reaction.emoji == "🪨":
              embed=discord.Embed(title="It's A Tie!", description="Both Players Chose Rock! It's A Tie!", color=16776960)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "🧾":
              embed=discord.Embed(title="You Win!", description="User Chose Paper & Bot Chose Rock! You Win!", color=65280)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "✂️":
              embed=discord.Embed(title="You Lose!", description="User Chose Scissors & Bot Chose Rock", color=16711680)
              await ctx.send(embed=embed)
              break
          
          elif rps_random == "p":
            if reaction.emoji == "🪨":
              embed=discord.Embed(title="You Lose!", description="User Chose Rock & Bot Chose Paper! You Lose!", color=16711680)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "🧾":
              embed=discord.Embed(title="It's A Tie!", description="Both Players Chose Paper! It's A Tie!", color=16776960)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "✂️":
              embed=discord.Embed(title="You Win!", description="User Chose Scissors & Bot Chose Paper! You Win!", color=65280)
              await ctx.send(embed=embed)
              break
          
          elif rps_random == "s":
            if reaction.emoji == "🪨":
              embed=discord.Embed(title="You Win!", description="User Chose Rock & Bot Chose Scissors! You Win!", color=65280)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "🧾":
              embed=discord.Embed(title="You Lose!", description="User Chose Paper & Bot Chose Scissors! You Lose!", color=16711680)
              await ctx.send(embed=embed)
              break
            
            elif reaction.emoji == "✂️":
              embed=discord.Embed(title="It's A Tie!", description="Both Players Chose Scissors! It's A Tie!", color=16776960)
              await ctx.send(embed=embed)
              break


          
      

def setup(client):
    client.add_cog(RPS(client))