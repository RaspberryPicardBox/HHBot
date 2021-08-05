# The HH Clan Discord Bot
# Written by RaspiBox

# --Imports--
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, MissingRequiredArgument, PrivateMessageOnly
from discord import NotFound, HTTPException
from aiohttp import ServerConnectionError
import logging
import asyncio
import datetime
from datetime import datetime
import json
import sys

# --Logging--
logger = logging.getLogger(__name__)
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)
logging.basicConfig(filename="HHBotLogs.log")

log = open("HHBotLogs.log", "a")
log.truncate(0)
log.close()


def handle_exception(exc_type, exc_value, exc_traceback):  # Thanks to Dennis Golomazov on Stack Overflow
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.error("{} Uncaught exception".format(datetime.datetime.now()), exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception

if __name__ == '__main__':
    description = "HHBot"

    token = ""

    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", description=description, intents=intents)
    client = discord.Client()


    async def get_json(filename):
        with open("{0}".format(filename)) as f:
            contents = json.load(f)
        f.close()
        return contents


    async def set_json(filename, contents):
        with open("{0}".format(filename), "a") as f:
            f.truncate(0)
            f.write(json.dumps(contents))
        f.close()


    @bot.event
    async def on_ready():
        print("Bot loaded and ready!")
        print("-----")
        print("Current time is {}".format(datetime.now()))

bot.run(token)
