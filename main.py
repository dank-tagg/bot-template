import discord
from discord.ext import commands

import os
from os import environ
from os.path import dirname, join

# REMINDER: SET THE CONFIGURATIONS IN THE .env FILE BEFORE RUNNING IT

# Loading .env file.
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Bot constructor, edit this to your needs.
bot = commands.Bot(prefix=environ.get("prefix"))

# Starting the bot
bot.run(environ.get("token"))
