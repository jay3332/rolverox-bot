from __future__ import annotations

import discord

from core.cog import Cog
import config

class Listeners(Cog):
    @Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        channel = self.bot.get_channel(config.join_channel)

        if channel is not None:
            assert isinstance(channel, discord.TextChannel)

            await channel.send(f'Welcome to the RolveroX server, {member.mention}!\n\nPlease take a look at <#970172089464152074>')

setup = Listeners.setup
