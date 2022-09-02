from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api.environments_for_db import get_buttons, db_buttons
from data.config import ADMINS
from utils.db_api.dbconfig import get, get_bot_id
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    bot_id = await get_bot_id(ADMINS[0])

    await get_buttons(bot_id)

    all_button = InlineKeyboardMarkup(row_width=1,
        inline_keyboard=[
            [InlineKeyboardButton(text=f'{buton["b"]}',url=f'{buton["r"]}')] for buton in db_buttons if buton != {}
        ]
    )


    main = await get("bots", bot_id, "main")
    await message.answer(f"{main}", reply_markup=all_button)
