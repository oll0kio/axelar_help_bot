from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.menu_keyboards import make_callback_data
from loader import dp
from utils.db_api.db_commands import add_new_user, count_users


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await add_new_user()
    text = ("101(Hello), {user}, my name is AxelarHelperBot!\n"
            "101(Привет), {user}, моё имя AxelarHelperBot!\n"
            "\n"
            "Thanks to me, {count_users} users learned more about the Axelar ecosystem!\n"
            "Благодаря мне подробнее об экосистеме Axelar узнало {count_users} пользователей!\n"
            "\n"
            "Please choose a language so I can continue the dialogue with you:\n"
            "Пожалуйста, выбери язык, чтобы мы могли продолжать с тобой диалог:\n"
            ).format(
        user=message.from_user.full_name, count_users=await count_users()
    )
    markup = InlineKeyboardMarkup(row_width=2)
    markup.row(InlineKeyboardMarkup(text="Русский", callback_data=make_callback_data(lang="ru")),
               InlineKeyboardMarkup(text="English", callback_data=make_callback_data(lang="en")))
    await message.answer(text, reply_markup=markup)