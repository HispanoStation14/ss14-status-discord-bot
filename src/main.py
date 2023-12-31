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
    status_response_content = status_response.json()
    server_status = ServerStatus(**status_response_content)
    await ctx.send(embed=generate_server_status_embed(server_status=server_status))

discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")

bot.run(token=discord_bot_token)
