from aiogram import types

from keyboards.inline.menu_keyboards import menu_keyboard, menu_cd, info_keyboard
from loader import dp


async def list_menu(callback: types.CallbackQuery, lang):
    markup = await menu_keyboard(lang)
    if lang == "ru":
        text = "абоба"
    else:
        text = "aboba"
    await callback.message.edit_text(text, reply_markup=markup)


async def show_info(callback: types.CallbackQuery, lang):
    markup = info_keyboard(lang)
    text = f"fds"
    await callback.message.edit_text(text, reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    lang = callback_data.get('lang')

    levels = {
        "0": list_menu,
        "1": show_info
    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        lang=lang
    )
