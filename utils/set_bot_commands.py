from aiogram import types
from aiogram.types import BotCommandScopeChat


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "✔ запустити бота"),
        ]
    )
