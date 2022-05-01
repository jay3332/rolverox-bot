from discord import TextChannel
from discord.ext.tasks import loop

from core.cog import Cog

class Stats(Cog):
    @loop(minutes=5)
    async def update_stats(self) -> None:
        await self.bot.wait_until_ready()

        guild = self.bot.get_guild(969411991506661449)
        assert guild is not None

        members_channel = self.bot.get_channel(970424062360842291)
        if members_channel is not None:
            assert isinstance(members_channel, TextChannel)

            await members_channel.edit(name=f'members-{guild.member_count}')

setup = Stats.setup
