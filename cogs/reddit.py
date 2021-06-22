import discord
import praw
import os
import random
import asyncio
from discord.ext import commands
from prawcore import NotFound, ServerError, Forbidden, InvalidToken, BadRequest, PrawcoreException, InvalidInvocation, RequestException, ResponseException

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
user_agent = os.getenv('USER_AGENT')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent,
                     check_for_async=False)


class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reddit(self, ctx, *, x: str):
        x = x.lower()
        x = x.split(" ")

        try:
          reddit.subreddits.search_by_name(x[0], exact=True)
          subreddit = reddit.subreddit(x[0])
          all_subs = []

          if len(x) == 1:
            submissions = subreddit.hot(limit=100)
          elif x[1] == "new":
            submissions = subreddit.new(limit=100)
          elif x[1] == "rising":
            submissions = subreddit.rising(limit=100)
          elif x[1] == "top":
            submissions = subreddit.top(limit=100)
          else:
            submissions = subreddit.hot(limit=100)


          for submission in submissions:
              all_subs.append(submission)

          random_sub = random.choice(all_subs)
          name = random_sub.title
          url = random_sub.url
          permalink = random_sub.permalink
          link = "http://www.reddit.com"+permalink
          icon = random_sub.author.icon_img
          
          await ctx.message.delete()

          if url.endswith(('.jpg', '.jpeg', '.png')):
            if subreddit.over18 or submission.over_18:
              if ctx.channel.is_nsfw():
                embed = discord.Embed(title=name, url=link, color=ctx.author.color)
                embed.add_field(name="Subreddit", value=f"r/{random_sub.subreddit}")
                embed.add_field(name="Upvotes & Comments", value=f"<:upvote:818144327611187222> {random_sub.score}"+" "+" "+f"💬 {random_sub.num_comments}")
                embed.set_author(name=f"u/{random_sub.author}", icon_url=icon)
                await ctx.send(embed=embed)
                await ctx.send("|| " + url + " ||")
              

              else:
                  embed = discord.Embed(description="**NSFW Subreddit/Post Detected! This Needs To Be A NSFW Channel!**", color=ctx.author.color)
                  embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                  await ctx.send(embed=embed)
            

            else:
              embed = discord.Embed(title=name, url=link, color=ctx.author.color)
              embed.add_field(name="Subreddit", value=f"r/{random_sub.subreddit}")
              embed.add_field(name="Upvotes & Comments", value=f"<:upvote:818144327611187222> {random_sub.score}"+" "+" "+f"💬 {random_sub.num_comments}")
              embed.set_author(name=f"u/{random_sub.author}", icon_url=icon)
              embed.set_image(url=url)
              embed.set_footer(text="Command Requested By {}".format (ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
              await ctx.send(embed=embed)

          elif "gallery" in url:
              if subreddit.over18 or submission.over_18:
                if ctx.channel.is_nsfw():
                  buttons = ['✅', '❌']
                  embed=discord.Embed(title="This Post Is A Gallery. Do you want to see it?", description="Prepare for images...", color=ctx.author.color)
                  sent = await ctx.send(embed=embed)
                  for i in range(len(buttons)):
                    await sent.add_reaction(buttons[i])
                  
                  while True:
                    try: 
                      reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)

                    except asyncio.TimeoutError:
                      await sent.delete()
                      break

                    else:
                      if reaction.emoji == "✅":
                        submission = reddit.submission(url=url)
                        for item in sorted(submission.gallery_data['items'], key=lambda x: x['id']):
                            media_id = item['media_id']
                            meta = submission.media_metadata[media_id]
                            if meta['e'] == 'Image':
                                source = meta['s']
                                await ctx.send(source['u'])
                      elif reaction.emoji == "❌":
                        await sent.delete()
                else:
                    embed = discord.Embed(description="**NSFW Subreddit/Post Detected! This Needs To Be A NSFW Channel!**", color=ctx.author.color)
                    embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                    await ctx.send(embed=embed)
              else:
                  buttons = ['✅', '❌']
                  embed=discord.Embed(title="This Post Is A Gallery. Do you want to see it?", description="Prepare for images...", color=ctx.author.color)
                  sent = await ctx.send(embed=embed)
                  for i in range(len(buttons)):
                    await sent.add_reaction(buttons[i])
                  
                  while True:
                    try: 
                      reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)

                    except asyncio.TimeoutError:
                      await sent.delete()
                      break

                    else:
                      if reaction.emoji == "✅":
                        submission = reddit.submission(url=url)
                        for item in sorted(submission.gallery_data['items'], key=lambda x: x['id']):
                            media_id = item['media_id']
                            meta = submission.media_metadata[media_id]
                            if meta['e'] == 'Image':
                                source = meta['s']
                                await ctx.send(source['u'])
                      elif reaction.emoji == "❌":
                        await sent.delete()

          else:
            if subreddit.over18 or submission.over_18:
              if ctx.channel.is_nsfw():
                  embed = discord.Embed(title=name, url=link, color=ctx.author.color)
                  embed.add_field(name="Subreddit", value=f"r/{random_sub.subreddit}")
                  embed.add_field(name="Upvotes & Comments", value=f"<:upvote:818144327611187222> {random_sub.score}"+" "+" "+f"💬 {random_sub.num_comments}")
                  embed.set_author(name=f"u/{random_sub.author}", icon_url=icon)
                  await ctx.send(embed=embed)
                  await ctx.send("|| " + url + " ||")
  
              else:
                  embed = discord.Embed(description="**NSFW Subreddit/Post Detected! This Needs To Be A NSFW Channel!**", color=ctx.author.color)
                  embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                  await ctx.send(embed=embed)
            

            else:
                embed = discord.Embed(title=name, url=link, color=ctx.author.color)
                embed.add_field(name="Subreddit", value=f"r/{random_sub.subreddit}")
                embed.add_field(name="Upvotes & Comments", value=f"<:upvote:818144327611187222> {random_sub.score}"+" "+" "+f"💬 {random_sub.num_comments}")
                embed.set_author(name=f"u/{random_sub.author}", icon_url=icon)
                embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=embed)
                await ctx.send(url)

        except NotFound:
          await ctx.send("Error, subreddit not found. Please check spelling and try again. ")
        except ServerError:
          await ctx.send("Server Error, please try again later. ")
        except Forbidden:
          await ctx.send("Error, forbidden access. ")
        except InvalidToken:
          await ctx.send("Error, invalid token. ")
        except BadRequest:
          await ctx.send("Error, bad request. ")
        except PrawcoreException:
          await ctx.send("Error, prawcore exception. ")
        except InvalidInvocation:
          await ctx.send("Error, invalid invocation. ")
        except RequestException:
          await ctx.send("Error, incomplete http request. ")
        except ResponseException:
          await ctx.send("Error, issue with complete http request. ")


      

    @reddit.error
    async def reddit_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguements (subreddit) and OPTIONAL (hot/top/rising/new). Ex. c!reddit dankmemes hot ")
      if isinstance(error, commands.BadArgument):
        await ctx.send("Error, subreddit not found. Try again. ")

def setup(client):
    client.add_cog(Reddit(client))