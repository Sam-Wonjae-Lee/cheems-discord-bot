import discord
import asyncio
from mediawiki import MediaWiki
from discord.ext import commands

class WIKI(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wiki(self, ctx, *, x: str,):
      wikipedia = MediaWiki()
      await ctx.message.delete()
      buttons = ["🔴","🟡","🟢", "🔵", "🟣"]
      embed=discord.Embed(title="Top 5 Search results for '{}': ".format(x), color=ctx.author.color)
      sent0 = await ctx.send(embed=embed)
      search = wikipedia.search(x)[0:5]
      results = search.copy()

      for i in range(5):
        search[i] = buttons[i] + " " + search[i]
      
      embed1=discord.Embed(description="\n".join(search), color=ctx.author.color)
      embed1.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
      sent = await ctx.send(embed=embed1)

      for i in range(5):
        await sent.add_reaction(buttons[i])

      while True:
        try:
            reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)

        except asyncio.TimeoutError:
          await sent0.delete()
          await sent.delete()

        else:
          if reaction.emoji == "🔴":
            p = wikipedia.page(results[0])
            await ctx.send(p.url)
            break
          elif reaction.emoji == "🟡":
            p = wikipedia.page(results[1])
            await ctx.send(p.url)
            break
          elif reaction.emoji == "🟢":
            p = wikipedia.page(results[2])
            await ctx.send(p.url)
            break
          elif reaction.emoji == "🔵":
            p = wikipedia.page(results[3])
            await ctx.send(p.url)
            break
          elif reaction.emoji == "🟣":
            p = wikipedia.page(results[4])
            await ctx.send(p.url)
            break

    @wiki.error
    async def wiki_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguements (search). Ex. c!wiki obama ")
      if isinstance(error, commands.BadArgument):
        await ctx.send("Error, wiki not found. Try again. ")
 
def setup(client):
    client.add_cog(WIKI(client))