from __future__ import annotations

from typing import TYPE_CHECKING

from discord.ext.commands import Cog as _Cog

if TYPE_CHECKING:
    from .bot import Rolverox


class Cog(_Cog):
    def __init__(self, bot: Rolverox) -> None:
        self.bot = bot
    
    @classmethod
    async def setup(cls, bot: Rolverox) -> None:
        await bot.add_cog(cls(bot))
