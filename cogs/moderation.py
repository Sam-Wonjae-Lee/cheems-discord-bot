import asyncio
import discord
import time
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Embed, Color
from typing import Optional
from pathlib import Path

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, *, amount: int,): 
        await ctx.channel.purge(limit=amount)
        if amount == 1:
         embed=discord.Embed(title="Deleted!", description=f"{amount} Message Was Deleted By {ctx.author.mention}", color=ctx.author.color)
         embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
         await ctx.send(embed=embed)
        elif amount-1 > 1:
         embed=discord.Embed(title="Deleted!", description=f"{amount} Messages Were Deleted By {ctx.message.author}", color=ctx.author.color)
         embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
         await ctx.send(embed=embed)

    @delete.error
    async def delete_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguement (number of messages to delete). Ex. c!delete 5 ")
      if isinstance(error, MissingPermissions):
          await ctx.send("❌ You don't have permission to delete messages (Manage messages required).")

    @commands.command(name="ban", aliases=['ban_user', 'delete_user'])
    @commands.has_permissions(ban_members=True)
    async def ban_command(self, ctx, user : discord.Member, *, reason):
        await user.ban(reason=reason)

        embed = Embed(color=discord.Color.red())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.message.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"BAN CASE | BY {ctx.author}",
                        value=f"The user {user.mention} has been banned from the guild.\nREASON: **{reason}**\nMODERATOR: {ctx.author.mention}")

        await ctx.send(embed=embed)

    @ban_command.error
    async def ban_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguements (user) and (reason). Ex. c!ban <user> <reason> ")
      if isinstance(error, commands.BadArgument):
        await ctx.send("Error, user not found. Try again. ")
      if isinstance(error, MissingPermissions):
          await ctx.send("❌ You don't have permission to ban users (Ban members required).")

    @commands.command(name="kick", aliases=['kick_user'])
    @commands.has_permissions(kick_members=True)
    async def kick_command(self, ctx, user : discord.Member, *, reason):
        await user.kick(reason=reason)

        embed = Embed(color=discord.Color.red())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.message.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"KICK CASE | BY {ctx.author}",
                        value=f"The user {user.mention} has been kicked from the guild.\nREASON: **{reason}**\nMODERATOR: {ctx.author.mention}")

        await ctx.send(embed=embed)

    @kick_command.error
    async def kick_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguements (user) and (reason). Ex. c!kick <user> <reason> ")
      if isinstance(error, commands.BadArgument):
        await ctx.send("Error, user not found. Try again. ")
      if isinstance(error, MissingPermissions):
          await ctx.send("❌ You don't have permission to kick users (Kick members required).")

    @commands.command(name="warn", aliases=['sudo'])
    @commands.has_permissions(kick_members=True)
    async def warn_command(self, ctx, user : discord.Member, *, reason):
        embed = Embed(color=discord.Color.gold())
        embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"Warning",
                        value=f"{user.mention} you got a warning in the guild from {ctx.author.mention} for the following reason:\n**{reason}**.\nPlease stop doing wrong!")

        await ctx.send(embed=embed)

    @warn_command.error
    async def warn_command_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguements (user) and (reason). Ex. c!warn <user> <reason> ")
      if isinstance(error, commands.BadArgument):
        await ctx.send("Error, user not found. Try again. ")
      if isinstance(error, MissingPermissions):
          await ctx.send("❌ You don't have permission to warn users (Kick members required).")

def setup(client):
    client.add_cog(Moderation(client))
