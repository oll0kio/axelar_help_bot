from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData("show_menu", "level", "info", "lang")


def make_callback_data(level, info=0, lang="ru"):
    return menu_cd.new(level=level, info=info, lang=lang)


async def menu_keyboard(lang):
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=1)
    if lang == "ru":
        markup.add(InlineKeyboardMarkup(text="Сайт Axelar", url="https://axelar.network/"),
                   InlineKeyboardMarkup(text="Твитер Axelar", url="https://twitter.com/axelarcore"),
                   InlineKeyboardMarkup(text="Дискорд Axelar", url="https://discord.com/invite/aRZ3Ra6f7D"))
        markup.row(InlineKeyboardMarkup(text="Русский", callback_data=make_callback_data(lang="ru")),
                   InlineKeyboardMarkup(text="English", callback_data=make_callback_data(lang="en")))

    else:
        markup.add(InlineKeyboardMarkup(text="Axelar site", url="https://axelar.network/"),
                   InlineKeyboardMarkup(text="Axelar twitter", url="https://twitter.com/axelarcore"),
                   InlineKeyboardMarkup(text="Axelar discord", url="https://discord.com/invite/aRZ3Ra6f7D"))
        markup.row(InlineKeyboardMarkup(text="Русский", callback_data=make_callback_data(lang="ru")),
                   InlineKeyboardMarkup(text="English", callback_data=make_callback_data(lang="en")))
    return markup


def info_keyboard(lang):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup()
    if lang == "ru":
        markup.row(
            InlineKeyboardMarkup(text="Назад", callback_data=make_callback_data(level=CURRENT_LEVEL - 1, lang=lang)),
        )
    else:
        markup.row(
            InlineKeyboardMarkup(text="Back", callback_data=make_callback_data(level=CURRENT_LEVEL - 1, lang=lang)),
        )
    return markup
