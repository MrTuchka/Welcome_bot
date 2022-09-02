from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.dbconfig import get_button, get_button_ref

b1 = get_button("1")
r1 = get_button_ref("1")

b2 = get_button("2")
r2 = get_button_ref("2")

b3 = get_button("3")
r3 = get_button_ref("3")

b4 = get_button("4")
r4 = get_button_ref("4")

b5 = get_button("5")
r5 = get_button_ref("5")

# you can configure more bot types here.
BOT_TEMPLATES = [
    {
        "button_text": "Створити Welcome Bot",
        "bot_id": "welcome_bot",
        "github_repo": "git@github.com:MrTuchka/Welcome_bot.git",
    },
    {
        "button_text": "Створити",
        "bot_id": "welcome_bot",
        "github_repo": "git@github.com:MrTuchka/Welcome_bot.git",
    }
]


all_button = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=f'{bot_template["button"]}',
                url=f"{bot_template['ref']}",
            ) for bot_template in BOT_TEMPLATES

        ],
    ]
)
