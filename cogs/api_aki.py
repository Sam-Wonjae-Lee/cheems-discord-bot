import discord
from discord.ext import commands
import akinator
import asyncio

class API_AKI(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.command()
    async def aki(self, ctx):
      await ctx.message.delete()
      loading = await ctx.send("Loading... ")
      force_ended = False
      buttons = ['◀️', '✅', '❌', '🤷‍♂️', '😕', '⁉️', '😔']
      aki = akinator.Akinator()
      q = aki.start_game()
      await loading.delete()
      target_progress = 80
      q_num = 1
      first_answer = True
      while True and not force_ended:
        while aki.progression <= target_progress:
          embed=discord.Embed(title=f"Q.{q_num} "+q + "\n\t", description="[ ◀️ (Back) / ✅ (Yes) / ❌ (No) / 🤷‍♂️ (Probably) / 😕 (Probably Not) / ⁉️ (Idk) / 😔 (End)]", color=ctx.author.color)
          embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
          sent = await ctx.send(embed=embed)
          q_num += 1
          for num_of_answers in range(len(buttons)):
            await sent.add_reaction(buttons[num_of_answers])
          try: 
              reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)
          except asyncio.TimeoutError:
              embed=discord.Embed(title="Times Up!", description="Your Time Has Ran Out! Try Again!", color = discord.Colour.red)
              await ctx.send(embed=embed)
              break
          else:
              if reaction.emoji == "◀️":
                try:
                    q = aki.back()
                    q_num -= 2
                except akinator.CantGoBackAnyFurther:
                    pass
              else:
                if reaction.emoji == "✅":
                  q = aki.answer("y")
                elif reaction.emoji == "❌":
                  q = aki.answer("n")
                elif reaction.emoji == "🤷‍♂️":
                  q = aki.answer("p")
                elif reaction.emoji == "😕":
                  q = aki.answer("pn") 
                elif reaction.emoji == "⁉️":
                  q = aki.answer("idk")
                elif reaction.emoji == "😔":
                  embed=discord.Embed(title="Ended...", description="Akinator Has Force Ended!", color=ctx.author.color)
                  await ctx.send(embed=embed)
                  force_ended = True
                  break

        if not force_ended:      
          aki.win()
          embed1=discord.Embed(title=f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?", color=ctx.author.color)
          embed1.set_image(url=aki.first_guess['absolute_picture_path'])
          sent2 =await ctx.send(embed=embed1)
          buttons2 = ['✅', '❌']

          for emojis in range(len(buttons2)):
            await sent2.add_reaction(buttons2[emojis])

          while True:
            try: 
              reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)
            except:
              embed=discord.Embed(title="Times Up!", description="Your Time Has Ran Out! Try Again!", color = discord.Colour.red)
              await ctx.send(embed=embed)
              break
          
            else:
              if reaction.emoji == '✅':
                if first_answer:
                  embed=discord.Embed(title="Yay, First Try!", color=discord.Colour.green())
                  await ctx.send(embed=embed)
                  force_ended = True
                  break
                else:
                  embed=discord.Embed(title="Yay", color=discord.Colour.green())
                  await ctx.send(embed=embed)
                  force_ended = True
                  break
                
              elif reaction.emoji == '❌':
                if aki.progression > 95:
                    force_eneded = True
                    embed=discord.Embed(title="You Have Defeated Me!", color=discord.Colour.red())
                    await ctx.send(embed=embed)
                    break
                target_progress = 95
                break
        
def setup(client):
    client.add_cog(API_AKI(client))