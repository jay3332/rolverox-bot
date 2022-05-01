from __future__ import annotations

import jishaku
from discord import Intents
from discord.ext.commands import Bot

import config

jishaku.Flags.NO_UNDERSCORE = True
jishaku.Flags.NO_DM_TRACEBACK = True


class Rolverox(Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix='r!',
            intents=Intents.all()
        )
    
    def run(self) -> None:
        super().run(token=config.token)
