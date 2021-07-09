# Imports the necessary libraries for Discord
from copy import copy
import discord
from discord.ext import commands
import json
import random

# Create the bot variable
bot = commands.Bot(command_prefix=["!liz ", "!Liz ","!b ", "!B "], owner_id=488130273662337034)

# Commands
@bot.command()
async def test(ctx):
    await ctx.send("Invite StalkerBot!")

# Run the bot
with open('config.json') as a:
    data = json.load(a)

bot.run(data['token'])