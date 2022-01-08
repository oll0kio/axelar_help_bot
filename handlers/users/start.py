from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api.db_commands import get_user_by_id, add_new_user, get_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    referral = message.get_args()
    user = await add_new_user(referral=referral)
    text = f'Добро пожаловать, {message.from_user.full_name}!\n'
    if user.referral:
        ref = await get_user_by_id(int(user.referral))
        text += f'Вас пригласил {ref.full_name} \n'
    await message.answer(text + f'Жми /menu')