from datetime import datetime

from discord import Embed
from pydantic import BaseModel


class ServerStatus(BaseModel):
    map: str
    name: str
    players: int
    tags: list[str]
    round_start_time: datetime | None
    soft_max_players: int
    run_level: int


def generate_server_status_embed(server_status: ServerStatus) -> Embed:
    # TODO: Parametrize these fields names
    server_status_embed = Embed(title="Estado de la estación")
    server_status_embed.add_field(name="Tripulantes", value=server_status.players)
    server_status_embed.add_field(name="Estación", value=server_status.map)
    server_status_embed.add_field(name="Servidor en el hub", value=server_status.name, inline=False)
    return server_status_embed
