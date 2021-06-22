import discord
from discord.ext import commands
import random
import asyncio


class SingleGames(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def coinguess(self, ctx):
      await ctx.message.delete()
      buttons=["🗣", "🦊"]
      embed=discord.Embed(title="Guess The Side!", description="Choose `Heads` Or `Tails` For Your Answer!", color=ctx.author.color)
      embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
      sent=await ctx.send(embed=embed)
      
      for button in buttons:
         await sent.add_reaction(button)
      

      while True:
        try:
            reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)

        except asyncio.TimeoutError:
            await sent.delete()
            embed=discord.Embed(title="Times Up!", description="Your Time Has Ran Out! Try Again!", color = discord.Colour.red())
            await ctx.send(embed=embed)
            break

        else:
          bot_guess="ht"
          bot_choice=random.choice(bot_guess)
          if bot_choice == "h":
           if reaction.emoji == "🗣":
              embed=discord.Embed(title="You Win!", description="Both User & Bot Said Heads! You Win!", color=65280)
              await ctx.send(embed=embed)
              break
           elif reaction.emoji == "🦊":
              embed=discord.Embed(title="You Lose!", description="User Said Tails & Bot Said Heads! You Lose!", color=16711680)
              await ctx.send(embed=embed)
              break
          elif bot_choice == "t":
            if reaction.emoji == "🗣":
              embed=discord.Embed(title="You Lose!", description="User Said Heads & Bot Said Tails! You Lose!", color=16711680)
              await ctx.send(embed=embed)
              break
            elif reaction.emoji == "🦊":
              embed=discord.Embed(title="You Win!", description="Both User & Bot Said Tails! You Win!", color=65280)
              await ctx.send(embed=embed)
              break
        





def setup(client):
    client.add_cog(SingleGames(client))