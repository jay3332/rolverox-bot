from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING, Any

from discord.ext.commands import Cog as _Cog, CogMeta
from discord.ext.tasks import Loop

if TYPE_CHECKING:
    from .bot import Rolverox
    from typing_extensions import Self

__log__ = logging.getLogger(__name__)

class CogMeta(CogMeta):
    if TYPE_CHECKING:
        __tasks__: list[Loop]


class MetaTask(CogMeta):
    """
    A simple Metclass that can be used to get all tasks.Loop from the class,
    to start and cancel them easily.
    """
    def __new__(cls, name: Any, bases: Any, attrs: Any, **kwargs: Any) -> Self:
        new_cls = super().__new__(cls, name, bases, attrs)
        _inner_tasks = [
            value
            for _, value in attrs.items()
            if issubclass(value.__class__, Loop)
        ]


        new_cls.__tasks__ = _inner_tasks  # type: ignore

        return new_cls

    def _unload_tasks(self) -> None:
        for task in self.__tasks__:
            coro = task.__dict__.get('coro')
            if not coro:
                continue

            __log__.info(
                f'Stopping task {coro.__name__} after {task.current_loop} intervals.'
            )

            loop = asyncio.get_running_loop()
            _tasks = []

            if task.is_running():
                task.cancel()
                _tasks.append(task._task)

            loop.create_task(asyncio.gather(*_tasks))  # type: ignore

    def _load_tasks(cls, self) -> None:
        for task in cls.__tasks__:
            coro = task.__dict__.get('coro')

            if not coro:
                continue

            __log__.info(
                f'Stopping task {coro.__name__} after {task.current_loop} intervals.'
            )

            if not task.is_running():
                task.start(self)


class Cog(_Cog, metaclass=MetaTask):
    def __init__(self, bot: Rolverox) -> None:
        self.bot = bot
    
    def cog_load(self) -> None:
        self.__class__._load_tasks(self)
    
    def cog_unload(self) -> None:
        self.__class__._unload_tasks()
    
    @classmethod
    async def setup(cls, bot: Rolverox) -> None:
        await bot.add_cog(cls(bot))
