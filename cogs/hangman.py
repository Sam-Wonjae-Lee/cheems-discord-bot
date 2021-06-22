import discord
from discord.ext import commands
import asyncio
import random
from words import word_list

class Hangman(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hangman(self, ctx):
      await ctx.message.delete()
      game_word = random.choice(word_list)
      game_word = list(game_word)
      user_words = []
      guessed_letters = []
      mistakes = 0 
  
      embed=discord.Embed(title="Hangman", description="Your Objetive Is To Guess The Word By Typing Your Letter!", color=ctx.author.color)
      embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
      await ctx.send(embed=embed)

      for i in range(len(game_word)):
        user_words.append("ㅡ")

      while mistakes <= 6:
        await ctx.send(display_hangman(mistakes))
        await ctx.send("".join(user_words))
        embed1=discord.Embed(title="Enter A Letter: ", color=ctx.author.color)
        await ctx.send(embed=embed1)

        try: 
          message = await self.client.wait_for("message", timeout = 60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
          guess = message.content
          guess = guess.lower()

        except asyncio.TimeoutError:
           embed=discord.Embed(title="Times Up!", description="Your Time Has Ran Out! Try Again! Your Word Was "+"".join(game_word).upper()+"!", color = discord.Colour.red())
           await ctx.send(embed=embed)
           break

        else:
          if len(guess) == 1 and guess.isalpha():
            if guess in game_word:
              if guess in guessed_letters:
                embed=discord.Embed(title="You Already Guessed That Letter!", color=ctx.author.color)
                await ctx.send(embed=embed)

              else:
                embed=discord.Embed(title="You Guessed A Letter!", color=discord.Colour.green())
                await ctx.send(embed=embed)
                for i in range(len(game_word)):
                   if guess == game_word[i]:
                     user_words[i] = guess

                guessed_letters.append(guess)


            elif guess not in game_word:
              if guess in guessed_letters:
                embed=discord.Embed(title="You Already Guessed That Letter!", color=ctx.author.color)
                await ctx.send(embed=embed)
              else: 
                embed=discord.Embed(title="That Letter Is Not In The Word!", color=discord.Colour.red())
                await ctx.send(embed=embed)
                mistakes += 1
                guessed_letters.append(guess)


          else:
            embed=discord.Embed(title="You Did Not Guess A Letter!", color=discord.Colour.red())
            await ctx.send(embed=embed)
            mistakes += 1
            guessed_letters.append(guess)


          if game_word == user_words:
            await ctx.send(display_hangman(mistakes))
            embed=discord.Embed(title="You Got The Word "+"".join(game_word).upper()+"! Congratulations!", color=discord.Colour.green())
            await ctx.send(embed=embed)
            break
          if mistakes >= 6:
            await ctx.send(display_hangman(mistakes))
            embed=discord.Embed(title="You Made Too Many Mistakes! The Answer Was "+"".join(game_word).upper()+"! Too Bad!", color=discord.Colour.red())
            await ctx.send(embed=embed)
            break


      

  

def display_hangman(mistakes):
    stages=['''
  +===+
 |         |
           |
           |
           |
           |
=========''', '''
  +===+
 |         |
O        |
           |
           |
           |
=========''', '''
  +===+
 |         |
O        |
 |         |
           |
           |
=========''', '''
   +===+
  |         |
 O        |
/|         |
            |
            |
 =========''', '''
  +===+
  |         |
 O        |
/|\       |
            |
            |
=========''', '''
  +===+
  |        |
 O       |
/|\      |
/         |
           |
=========''', '''
  +===+
  |        |
 O       |
/|\      |
/ \      |
           |
=========''']

    return stages[mistakes]

def setup(client):
    client.add_cog(Hangman(client))