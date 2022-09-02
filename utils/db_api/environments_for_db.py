from utils.db_api.dbconfig import get_field, get

db_buttons = [{}, {}, {}, {}, {}]

async def get_buttons(bot_id):
    b1 = await get_field("bots", bot_id, 'button1', "about")
    r1 = await get_field('bots', bot_id, 'button1', 'ref')
    if b1 == "🚫":
        db_buttons[0] = {}
    else:
        db_buttons[0] = {"b": b1, "r": r1}

    b2 = await get_field('bots', bot_id, 'button2', 'about')
    r2 = await get_field('bots', bot_id, 'button2', 'ref')
    if b2 == "🚫":
        db_buttons[1] = {}
    else:
        db_buttons[1] = {"b": b2, "r": r2}

    b3 = await get_field('bots', bot_id, 'button3', 'about')
    r3 = await get_field('bots', bot_id, 'button3', 'ref')
    if b3 == "🚫":
        db_buttons[2] = {}
    else:
        db_buttons[2] = {"b": b3, "r": r3}

    b4 = await get_field('bots', bot_id, 'button3', 'about')
    r4 = await get_field('bots', bot_id, 'button3', 'ref')
    if b4 == "🚫":
        db_buttons[3] = {}
    else:
        db_buttons[3] = {"b": b4, "r": r4}

    b5 = await get_field('bots', bot_id, 'button3', 'about')
    r5 = await get_field('bots', bot_id, 'button3', 'ref')
    if b5 == "🚫":
        db_buttons[4] = {}
    else:
        db_buttons[4] = {"b": b5, "r": r5}


