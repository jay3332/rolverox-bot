from __future__ import annotations

import os

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
            intents=Intents.all(),
        )
        self.owner_ids = {482665245928849408, 590323594744168494}

    async def load_all_extensions(self) -> None:
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')

        await self.load_extension('jishaku')
    
    async def on_ready(self) -> None:
        print(f'Logged in as {str(self.user)}')
    
    def run(self) -> None:
        super().run(token=config.token)
