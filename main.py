import os
from os import environ
from os.path import dirname, join

import discord
from discord.ext import commands
from dotenv import load_dotenv

# REMINDER: SET THE CONFIGURATIONS IN THE .env FILE BEFORE RUNNING IT

# Loading .env file.
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Bot constructor, edit this to your needs.
bot = commands.Bot(command_prefix="?")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


# Starting the bot
bot.run(environ.get("token"))
