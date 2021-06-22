import discord
from discord.ext import commands
import asyncio
import random

class Diceguess(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def diceguess(self, ctx):
      await ctx.message.delete()
      buttons=["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
      embed=discord.Embed(title="Guess The Number!", description="Try To Guess What The Bot Is Thinking! \nChoose Any Number For Your Answer!", color=ctx.author.color)
      embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
      sent=await ctx.send(embed=embed)
      
      for button in buttons:
         await sent.add_reaction(button)


      while True:
        try:
            reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=5.0)

        except asyncio.TimeoutError:
            await sent.delete()
            embed=discord.Embed(title="Times Up!", description="Your Time Has Ran Out! Try Again!", color = discord.Colour.red())
            await ctx.send(embed=embed)
            break

        else:
          num_guess=random.randint(1,6)
          if num_guess == 1 and reaction.emoji == "1️⃣":
            embed=discord.Embed(title="You Win!", description="Both User & Bot Guessed Number One! You Win!", color=65280)
            await ctx.send(embed=embed)
            break
          elif num_guess == 2 and reaction.emoji == "2️⃣":
            embed=discord.Embed(title="You Win!", description="Both User & Bot Guessed Number Two! You Win!", color=65280)
            await ctx.send(embed=embed)
            break
          elif num_guess == 3 and reaction.emoji == "3️⃣":
            embed=discord.Embed(title="You Win!", description="Both User & Bot Guessed Number Three! You Win!", color=65280)
            await ctx.send(embed=embed)
            break
          elif num_guess == 4 and reaction.emoji == "4️⃣":
            embed=discord.Embed(title="You Win!", description="Both User & Bot Guessed Number Four! You Win!", color=65280)
            await ctx.send(embed=embed)
            break
          elif num_guess == 5 and reaction.emoji == "5️⃣":
            embed=discord.Embed(title="You Win!", description="Both User & Bot Guessed Number Five! You Win!", color=65280)
            await ctx.send(embed=embed)
            break
          elif num_guess == 6 and reaction.emoji == "6️⃣":
            embed=discord.Embed(title="You Win!", description="Both User & Bot Guessed Number Six! You Win!", color=65280)
            await ctx.send(embed=embed)
            break
          elif num_guess == 2 and reaction.emoji == "1️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 1 & Bot Guessed Number 2!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 3 and reaction.emoji == "1️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 1 & Bot Guessed Number 3!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 4 and reaction.emoji == "1️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 1 & Bot Guessed Number 4!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 5 and reaction.emoji == "1️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 1 & Bot Guessed Number 5!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 6 and reaction.emoji == "1️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 1 & Bot Guessed Number 6!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 1 and reaction.emoji == "2️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 2 & Bot Guessed Number 1!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 3 and reaction.emoji == "2️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 2 & Bot Guessed Number 1!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 4 and reaction.emoji == "2️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 2 & Bot Guessed Number 4!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 5 and reaction.emoji == "2️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 2 & Bot Guessed Number 5!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 6 and reaction.emoji == "2️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 2 & Bot Guessed Number 6!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 1 and reaction.emoji == "3️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 3 & Bot Guessed Number 1!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 2 and reaction.emoji == "3️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 3 & Bot Guessed Number 2!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 4 and reaction.emoji == "3️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 3 & Bot Guessed Number 4!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 5 and reaction.emoji == "3️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 3 & Bot Guessed Number 5!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 6 and reaction.emoji == "3️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 3 & Bot Guessed Number 6!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 1 and reaction.emoji == "4️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 4 & Bot Guessed Number 1!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 2 and reaction.emoji == "4️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 4 & Bot Guessed Number 2!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 3 and reaction.emoji == "4️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 4 & Bot Guessed Number 3!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 5 and reaction.emoji == "4️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 4 & Bot Guessed Number 5!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 6 and reaction.emoji == "4️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 4 & Bot Guessed Number 6!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 1 and reaction.emoji == "5️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 5 & Bot Guessed Number 1!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 2 and reaction.emoji == "5️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 5 & Bot Guessed Number 2!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 3 and reaction.emoji == "5️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 5 & Bot Guessed Number 3!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 4 and reaction.emoji == "5️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 5 & Bot Guessed Number 4!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 6 and reaction.emoji == "5️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 5 & Bot Guessed Number 6!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 1 and reaction.emoji == "6️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 6 & Bot Guessed Number 1!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 2 and reaction.emoji == "6️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 6 & Bot Guessed Number 2!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 3 and reaction.emoji == "6️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 6 & Bot Guessed Number 3!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 4 and reaction.emoji == "6️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 6 & Bot Guessed Number 4!", color=16711680)
            await ctx.send(embed=embed)
            break
          elif num_guess == 5 and reaction.emoji == "6️⃣":
            embed=discord.Embed(title="You Lose!", description="User Guessed Number 6 & Bot Guessed Number 1!", color=16711680)
            await ctx.send(embed=embed)
            break
          

def setup(client):
    client.add_cog(Diceguess(client))