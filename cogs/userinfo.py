import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        await ctx.message.delete()
        
        if not member:
            member = ctx.message.author
        userAvatar = member.avatar_url
        embed = discord.Embed(title="User Information", color=ctx.author.color)
        embed.set_thumbnail(url=userAvatar)

        fields = [("Name", str(member), True), ("ID", member.id, True), ("Top Role", member.top_role.mention, True), ("Account Created (UTC)", member.created_at.strftime("%m/%d/%Y %H:%M:%S"), True), ("Account Joined (UTC)", member.joined_at.strftime("%m/%d/%Y %H:%M:%S"), True), ("Boosted", bool(member.premium_since), True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        embed.set_footer(text="Command Requested By {}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Error, please enter the required arguements (user). Ex. c!info <user> ")
      if isinstance(error, commands.BadArgument):
        await ctx.send("Error, user not found. Try again. ")

    


def setup(client):
    client.add_cog(Info(client))