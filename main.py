import discord
import os
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='c!', case_insensitive=True, help_command=None)


for filename in os.listdir('./cogs'): 
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))
