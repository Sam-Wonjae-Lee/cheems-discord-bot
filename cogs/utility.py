import discord
from discord.ext import commands
import random
class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dice(self, ctx):
     rand_dice = random.randint(1, 6)
     em = discord.Embed(description = f"**Your Final Roll Is: {rand_dice}**", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.message.delete()
     await ctx.send(embed=em)

    @commands.command(pass_context=True)
    async def poll(self, ctx, question, *options: str):
        await ctx.message.delete()
        if len(options) <= 1:
            embed=discord.Embed(title="📊 Poll", description="You Need More Than One Option To Make A Poll!", color=ctx.author.color)
            embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
            return
        if len(options) > 10:
            embed=discord.Embed(title="📊 Poll", description="You Cannot Make A Poll With More Than Ten Options!", color=ctx.author.color)
            embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
            return

        if len(options) == 2 and options[0].lower() == 'yes' and options[1].lower() == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=f"📊 {question}", description=''.join(description), color=ctx.author.color)
        embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        await react_message.edit_message(embed=embed)

    @poll.error
    async def poll_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguements (One Sentence With Quotaion & Two Options Required). Ex. c!poll 'Do You Like Ice Cream' 'Yes' 'No' 'Idk'. Remember SPACES and QUOTES. ")
      if isinstance(error, commands.BadArgument):
        await ctx.send("Error, bad arugument. Try again. ")

    @commands.command()
    async def eightball(self, ctx, *, question: str):
      await ctx.message.delete()
      eightball_ans = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]
      embed=discord.Embed(title=f":8ball: {question}", description=f"My Whimsical Answer Is: \n **{random.choice(eightball_ans)}**", color=ctx.author.color)
      embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
      await ctx.send(embed=embed)

    @eightball.error
    async def eightball_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguements (Question). Ex. c!eightball Is SamuelTheManual Smexy? ")
      if isinstance(error, commands.BadArgument):
        await ctx.send("Error, bad arugument. Try again. ")


def setup(client):
    client.add_cog(Utility(client))
