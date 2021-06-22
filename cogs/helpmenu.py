import discord
from discord.ext import commands
import asyncio

page1 = discord.Embed(title= "Cheems Help - `Created By CA1V1N & SamuelTheManual`", description="My Prefix Is `c!` [Invite Link](https://discord.com/api/oauth2/authorize?client_id=843502995147718676&permissions=3959909462&scope=bot)\n\nReact With ❌ To Delete This Message!\nUse The Arrows To Scroll Through Commands! \n\nUse `c!info <command name>` For Extended Info!\n Example: `c!info reddit`, `c!info joke`", colour=discord.Colour.red())
page1.add_field(name="Categories", value="<:1307793940001:816484124168683540>`Fun` - Have A Great Time With Our Silly Commands! \n<:fatyoshi:816489219996254229>`Mods` - Easy To Use Commands To Manage Your Server! 🎮`Games` - Play Exciting Single & Multiplayer Games! \n🛠️`Utility` - Very Useful Commands!")
page1.set_thumbnail(url="https://cdn.discordapp.com/avatars/815270826420469811/d842498ecdebc1a4fec34788e725b451.webp?size=1024")

page2 = discord.Embed(title="Fun!", description="Use `c!info <command name>` For Extended Info!\n Example: `c!info reddit`, `c!info joke` ", colour=discord.Colour.orange())
page2.add_field(name="Fun Commands", value="`c!catto` - Sends All The Cat Pics \n`c!doggo` - Sends All The Dog Pics \n`c!facts` - Sends All The Facts You Need \n`c!joke` - Jokes For Everyone \n`c!dadjoke` - The Better Or Worse Version \n`c!eightball` - Answers All Of Your Questions \n`c!waifu` - Sends 2D Galore (Needs Category) \n`c!waifunsfw` - Very Risque (For NSFW/Needs Category) \n`c!reddit` - Literally Provides All Subreddits With Any Category")

page3 = discord.Embed(title="Moderation!", description="Use `c!info <command name>` For Extended Info!\n Example: `c!info warn`, `c!info kick` ", colour=discord.Colour.gold())
page3.add_field(name="Moderation Commands (Only Admins Can Use)", value="`c!delete` - Deletes Messages (Number Required) \n`c!ban` - Bans A Member (Member Mention Required) \n`c!kick` - Kicks A Member (Member Mention Required) \n`c!warn` - Sends A Warning (Warning Message Required)")

page4=discord.Embed(title="Games!", description="Use `c!info <command name>` For Extended Info!\n Example: `c!info trivia`, `c!info hangman` ", color=discord.Colour.green())
page4.add_field(name="Games Command", value="`c!aki` - Play The Aki Game In Discord \n`c!trivia` - Test Your Knowledge \n`c!coinguess` - Choose Between Heads & Tails \n`c!diceguess` - Choose Between 1 & 6 \n`c!hangman` - Hangman In Discord \n`c!rps` - Rock Paper Scissors In Discord \n`c!rr` - Russian Roulette In Discord")

page5=discord.Embed(title="Utility!", description="Use `c!info <command name>` For Extended Info!\n Example: `c!info poll`, `c!info wiki`", color=discord.Colour.blue())
page5.add_field(name="Utility Commands", value="`c!bible` - In The Beginning God Created Discord \n`c!quote` - A Random Quote Keeps Me Up Today \n`c!userinfo` - Gives Info Of Member (Mention Required) \n`c!coin` - Flips A Coin \n`c!dice` - Rolls A Dice \n`c!poll` - Vote For Poll (1 Sentence & Minimum 2 Options Required) \n`c!wiki` - Wiki In Discord \n`c!weather` - Shows Weather From City (City Name Required)")

page6=discord.Embed(title="Our website!", description="[Check it for information and to give feedback!](https://cheemsdiscordbot.xyz/)", color=discord.Colour.purple())


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.help_pages = [page1, page2, page3, page4, page5, page6]
  
    @commands.command(name="help", aliases=['helpmenu', 'helpme', 'cheemshelp'])
    async def help(self, ctx):
       await ctx.message.delete()
       page1.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
       buttons = [u"\u23EA", "⬅️", "➡️", u"\u23E9", "❌"] 
       current = 0
       msg = await ctx.send(embed=self.client.help_pages[current])
    
       for button in buttons:
         await msg.add_reaction(button)

       while True:
        try:
            reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            await msg.delete()
            break

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0
                
            elif reaction.emoji == "⬅️":
                if current > 0:
                    current -= 1
                    
            elif reaction.emoji == "➡️":
                if current < len(self.client.help_pages)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(self.client.help_pages)-1
            
            elif reaction.emoji == "❌":
                await msg.delete()
                break

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=self.client.help_pages[current])

 
def setup(client):
    client.add_cog(Help(client))
