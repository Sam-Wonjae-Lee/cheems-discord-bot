import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def info(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Command Info - For Examples & Clarification", description = "Use `c!info <command name>` For Extended Info!\n Example: `c!info reddit`, `c!info joke` \n", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def joke(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Joke", description = "Tells You A Random Joke Everytime \nExample: `c!joke`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)

    @info.command()
    async def dadjoke(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Dad Joke", description = "Tells You A Random Dad Joke Everytime \nExample: `c!dadjoke`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def catto(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Catto", description = "Gives Cat Pics Galore\nExample: `c!catto`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)

    @info.command()
    async def doggo(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Doggo", description = "Gives Dog Pics Galore\nExample: `c!doggo`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def waifu(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Waifu", description = "Gives Anime Waifus Pics/Gifs (Must Include Category) \nExample: `c!waifu slap`, `c!waifu cringe`", color = ctx.author.color)
     em.add_field(name = "Waifu Categories", value = "waifu \nshinobu \nneko \nmegumin \nbully \ncuddle \ncry \nhug \nawoo \nkiss \nlick \npat \nsmug \nbonk \nyeet \nblush \nsmile \nwave \nhighfive \nhandhold \nnom \nbite \nglomp \nkill \nslap \nhappy \nwink \npoke \ndance \ncringe \nblush")
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def waifunsfw(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Waifu NSFW", description = "Gives NSFW Anime Waifus Pics/Gifs (Must Include Category & Only Works In NSFW Channels) \nExample: `c!waifunsfw waifu`, `c!waifu trap`", color = ctx.author.color)
     em.add_field(name = "Waifu NSFW Categories", value = "waifu \nneko \ntrap \nblowjob")
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def facts(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Facts", description = "Gives Random Facts\nExample: `c!facts`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def eightball(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Magic Eightball", description = "The Magic Eightball To Answer All Of Your Questions\nExample: `c!eightball Is SamuelTheManual Smexy?`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def delete(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Delete", description = "Only For Admins & Deletes Messages (Specific Number Required)\nExample: `c!delete 5`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def ban(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Ban", description = "Only For Admins & Bans Members (Mention Required)\nExample: `c!ban @Glerf`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def kick(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Kick", description = "Only For Admins & Kicks Members (Mention Required)\nExample: `c!kick @Glerf`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def warn(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Warn", description = "Only For Admins & Warns Members (Mention & Message Required)\nExample: `c!warn @SamuelTheManual Stop It`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def aki(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Akinator", description = "Akinator In Discord; Use Reactions To Select Answer \nExample: `c!aki`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def trivia(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Trivia", description = "Random Trivia Question To Answer; Use Reactions To Select Answer \nExample: `c!trivia`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def coinguess(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Coin Guess", description = "Guess Cheems's Choice With Heads & Tails; Use Reactions To Select Answer \nExample: `c!coinguess`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def diceguess(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Coin Guess", description = "Guess Cheems's Choice With 1 To 6; Use Reactions To Select Answer \nExample: `c!diceguess`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def hangman(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Hangman", description = "Answer By Entering A Letter; 1 Minute Timeout \nExample: `c!hangman`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def rps(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Rock Paper Scissors", description = "Guess Cheems's Choice With Rock Paper Scissors; Use Reactions To Select Answer \nExample: `c!rps`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def rr(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Russian Roulette", description = "Decide Your Fate With One Command \nExample: `c!rr`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)

    @info.command()
    async def quote(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Quote", description = "Gives A Random Quote For Inspiration \nExample: `c!quote`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def userinfo(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "User Info", description = "Provides User Info & Mention Required \nExample: `c!userinfo @SamuelTheManual`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def coin(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Coin", description = "Flips A Coin For You \nExample: `c!coin`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def dice(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Dice", description = "Gives A Random Number From 1 To 6 \nExample: `c!dice`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def poll(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Poll", description = "Prints A Poll For Democracy (One Sentence With Quotaion & Two Options Required)\nExample: `c!poll 'Do You Like Ice Cream' 'Yes' 'No' 'Idk'` ", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def bible(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Bible", description = "Gives Verses From The Bible (Chapter & Verse Required)\nExample: `c!bible genesis 1:1`, `c!bible john 1:1-4` ", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def wiki(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Wikipedia", description = "Provides A Wiki Page With Search Engine (Search Required & Use Reactions To Choose)\nExample: `c!wiki obama ", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def reddit(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Reddit", description = "Gives Post From Any Public Subreddit Including NSFW (Only For NSFW Channels)\nCan Choose From Hot, New, Rising, Top Of All Time\nIf There Is No Secondary Option It Will Automatically Choose Hot\nExample: `c!reddit pics rising`, `c!reddit nsfw top`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)
    
    @info.command()
    async def weather(self, ctx):
     await ctx.message.delete()
     em = discord.Embed(title = "Weather", description = "Shows Weather Live From City\nExample: `c!weather toronto`, `c!weather birmingham`", color = ctx.author.color)
     em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
     await ctx.send(embed = em)



    



def setup(client):
    client.add_cog(Info(client))