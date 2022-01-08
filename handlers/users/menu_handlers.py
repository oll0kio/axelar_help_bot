from typing import Union

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.menu_keyboards import menu_keyboard, services_keyboard, menu_cd, service_keyboard
from loader import dp
from utils.db_api.db_commands import get_service


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await list_menu(message)


async def list_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await menu_keyboard()
    if isinstance(message, types.Message):
        await message.answer(f'Здесь вы найдете необходимые реф. и не реф. ссылки'
                             f'\n(С МАКСИМАЛЬНЫМ БОНУСОМ)\nПоддержите любимого '
                             f'инфлюенера (и разработчика бота), пользуясь этими ссылкам', reply_markup=markup)
    elif isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text(f"Здесь вы найдете необходимые реф. и не реф. ссылки"
                                     f"\n(С МАКСИМАЛЬНЫМ БОНУСОМ)\nПоддержите любимого "
                                     f"инфлюенера (и разработчика бота), пользуясь этими ссылкам",
                                     reply_markup=markup)


async def list_services(callback: types.CallbackQuery, category, **kwargs):
    markup = await services_keyboard(category)
    await callback.message.edit_text(f"Вы выбрали категорию {category}", reply_markup=markup)


async def show_service(callback: types.CallbackQuery, category, service_id):
    service = await get_service(service_id)
    markup = service_keyboard(category, service)
    text = f"{service}"
    await callback.message.edit_text(text, reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category = callback_data.get('category')
    service_id = int(callback_data.get('service_id'))

    levels = {
        "0": list_menu,
        "1": list_services,
        "2": show_service
    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        category=category,
        service_id=service_id
    )
