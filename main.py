import os

import requests
from discord import Intents
from discord.ext import commands

from server_status import ServerStatus, generate_server_status_embed

bot = commands.Bot(
    command_prefix="/",
    description="",
    intents=Intents(members=True, message_content=True, messages=True),
)

SERVER_STATUS_ENDPOINT: str = os.getenv("SERVER_STATUS_ENDPOINT")


@bot.command()
async def status(ctx):
    status_response = requests.get(SERVER_STATUS_ENDPOINT)
    server_status = ServerStatus(**status_response.json())
    await ctx.send(embed=generate_server_status_embed(server_status=server_status))


bot.run(token=os.getenv("BOT_TOKEN"))