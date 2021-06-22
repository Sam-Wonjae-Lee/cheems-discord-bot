import discord
from discord.ext import commands
import json
import requests
import random
import html
import asyncio

class API(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx, *, x: str,):
        x = "".join(x)
        response = requests.get("https://goweather.herokuapp.com/weather/" + x)
        weather_json_data = json.loads(response.text)
        temperature = weather_json_data['temperature']
        temperature = temperature.replace("째", "°")
        description = weather_json_data['description']
        wind = weather_json_data['wind']

        if temperature != "":
          em = discord.Embed(title="Weather: \nThe Temperature For {} Currently Is {}! \nDescription: {}\nWind: {} ".format(x.title(), temperature, description, wind), color=ctx.author.color)
          em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
          await ctx.send(embed=em)
        else:
          await ctx.send("City not found. Please try again. Ex. c!weather <city> ")

    @weather.error
    async def weather_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguement (city). Ex. c!weather <city> ")

    @commands.command()
    async def bible(self, ctx, x: str, y: str):

        response = requests.get("https://bible-api.com/" + x + "%20" + y)
        bible_json_data = json.loads(response.text)

        if 'text' in bible_json_data:
          bible = bible_json_data['text']
          em = discord.Embed(title="Bible!", description=f"{bible}", color=ctx.author.color)
          em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)

          await ctx.message.delete()
          await ctx.send(embed=em)

        elif 'error' in bible_json_data:
          await ctx.send("Error, verse/passage not found. Please try again. Ex. c!bible genesis 1:1, c!bible john 1:1-4 ")

    @bible.error
    async def bible_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, verse/passage not found due to missing arguements (Chapter & Verse Required). Please try again. Ex. c!bible genesis 1:1, c!bible john 1:1-4 ")
    
    @commands.command()
    async def waifu(self, ctx, x: str):
        await ctx.message.delete()
        response = requests.get("https://waifu.pics/api/sfw/" + x)
        waifu_json_data = json.loads(response.text)
        waifu_pic = waifu_json_data["url"]
        em=discord.Embed(color=ctx.author.color)
        em.set_image(url=f"{waifu_pic}")
        em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)

    @waifu.error
    async def waifu_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, missing arugements. Required <category>. Catagories: waifu, shinobu, neko, megumin ,bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, kill, slap, happy, wink, poke, dance, cringe, blush. Ex. c!waifu slap   ")
       
    @commands.command()
    async def waifunsfw(self, ctx, x: str):
        if ctx.channel.is_nsfw():
            await ctx.message.delete()
            response = requests.get("https://waifu.pics/api/nsfw/" + x)
            waifu_nsfw_json_data = json.loads(response.text)
            waifu_nsfw_pic = waifu_nsfw_json_data["url"]
            await ctx.send("|| " + waifu_nsfw_pic + " ||")

            
        else:
            em = discord.Embed(title="Oops",
                               description="This Needs To Be A NSFW Channel",
                               color=ctx.author.color)
            await ctx.message.delete()
            await ctx.send(embed=em)

    @waifunsfw.error
    async def waifunsfw_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, missing arugements. Required <category>. Catagories: waifu, neko, trap, blowjob. Ex. c!waifunsfw neko")
          
    @commands.command()
    async def quote(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        quote_json_data = json.loads(response.text)
        quote = quote_json_data[0]['q'] + " -" + quote_json_data[0]['a']
        await ctx.message.delete()
        em = discord.Embed(title="Quote!", description = quote, color=ctx.author.color)
        em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)
        

    @commands.command()
    async def joke(self, ctx):
        response = requests.get(
            "https://official-joke-api.appspot.com/random_joke")
        joke_json_data = json.loads(response.text)
        joke = joke_json_data['setup'] + " " + joke_json_data['punchline']
        await ctx.message.delete()
        em = discord.Embed(title="Joke!", description=joke, color=ctx.author.color)
        em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    async def dadjoke(self, ctx):
        response = requests.get(
            "https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes"
        )
        dadjoke_json_data = json.loads(response.text)
        dadjoke = dadjoke_json_data['setup'] + " " + dadjoke_json_data[
            'punchline']
        await ctx.message.delete()
        em = discord.Embed(title="Dad Joke!", description=dadjoke, color=ctx.author.color)
        em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    async def catto(self, ctx):
        await ctx.message.delete()
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        cat_json_data = json.loads(response.text)
        cat = cat_json_data[0]['url']
        em=discord.Embed(color=ctx.author.color)
        em.set_image(url=f"{cat}")
        em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    async def doggo(self, ctx):
        await ctx.message.delete()
        response = requests.get("https://api.thedogapi.com/v1/images/search")
        dog_json_data = json.loads(response.text)
        dog = dog_json_data[0]['url']
        em=discord.Embed(color=ctx.author.color)
        em.set_image(url=f"{dog}")
        em.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command()
    async def trivia(self, ctx):
        await ctx.message.delete()
        wrong = False
        answers = []
        buttons = ["🔴","🟡","🟢", "🔵"]
        response = requests.get("https://opentdb.com/api.php?amount=1")
        trivia_json_data = json.loads(response.text)
        question = trivia_json_data['results'][0]["question"]
        correct_answers = trivia_json_data['results'][0]["correct_answer"]
        incorrect_answers = trivia_json_data['results'][0]["incorrect_answers"]

        embed=discord.Embed(title=f"{html.unescape(question)}", description="Show off your knowlege! Choose the correct answer! ", color=ctx.author.color)
        embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        sent1=await ctx.send(embed=embed)

        answers.append(correct_answers)

        for i in range(len(incorrect_answers)):
          answers.append(incorrect_answers[i])
      
        if len(answers) > 2:
          random.shuffle(answers)

        show_answers = answers.copy()

        for i in range(len(show_answers)):
          show_answers[i] = buttons[i] + " " + html.unescape(show_answers[i])

        embed=discord.Embed(title="\n".join(show_answers), color=ctx.author.color)
        sent2 = await ctx.send(embed=embed)

        for num_of_answers in range(len(show_answers)):
          await sent2.add_reaction(buttons[num_of_answers])

        while True:
          try:
              reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)

          except asyncio.TimeoutError:
              if answers.index(correct_answers) == 0:
                embed=discord.Embed(title="Times up! The Answer Is 🔴", color=16711680)
                await ctx.send(embed=embed)
              elif answers.index(correct_answers) == 1:
                mbed=discord.Embed(title="Times up! The Answer Is 🟡", color=16711680)
                await ctx.send(embed=embed)
              elif answers.index(correct_answers) == 2:
                embed=discord.Embed(title="Times up! The Answer Is 🟢", color=16711680)
                await ctx.send(embed=embed)
              elif answers.index(correct_answers) == 3:
                embed=discord.Embed(title="Times up! The Answer Is 🔵", color=16711680)
                await ctx.send(embed=embed)
            
              await sent1.delete()
              await sent2.delete()
              break

          else:
              if reaction.emoji == "🔴":
                if answers.index(correct_answers) == 0:
                  embed=discord.Embed(title="Correct! The Answer Is 🔴", color= 65280)
                  await ctx.send(embed=embed)
                  break
                else:
                  wrong = True
                  break
              elif reaction.emoji == "🟡":
                if answers.index(correct_answers) == 1:
                  embed=discord.Embed(title="Correct! The Answer Is 🟡", color= 65280)
                  await ctx.send(embed=embed)
                  break
                else:
                  wrong = True
                  break
              elif reaction.emoji == "🟢":
                if answers.index(correct_answers) == 2:
                  embed=discord.Embed(title="Correct! The Answer Is 🟢", color= 65280)
                  await ctx.send(embed=embed)
                  break
                else:
                  wrong = True
                  break
              elif reaction.emoji == "🔵":
                if answers.index(correct_answers) == 3:
                  embed=discord.Embed(title="Correct! The Answer Is 🔵", color= 65280)
                  await ctx.send(embed=embed)
                  break
                else:
                  wrong = True
                  break

        if wrong:
          if answers.index(correct_answers) == 0:
            embed=discord.Embed(title="Incorrect! The Answer Is 🔴", color=16711680)
            await ctx.send(embed=embed)
          elif answers.index(correct_answers) == 1:
            embed=discord.Embed(title="Incorrect! The Answer Is 🟡", color=16711680)
            await ctx.send(embed=embed)
          elif answers.index(correct_answers) == 2:
            embed=discord.Embed(title="Incorrect! The Answer Is 🟢", color=16711680)
            await ctx.send(embed=embed)
          elif answers.index(correct_answers) == 3:
            embed=discord.Embed(title="Incorrect! The Answer Is 🔵", color=16711680)
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(API(client))
