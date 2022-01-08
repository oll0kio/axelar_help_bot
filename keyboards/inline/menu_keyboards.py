from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from utils.db_api.db_commands import get_categories, count_services, get_services

menu_cd = CallbackData("show_menu", "level", "category", "service_id")


def make_callback_data(level, category="0", service_id="0"):
    return menu_cd.new(level=level, category=category, service_id=service_id)


async def menu_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=4)

    categories = await get_categories()

    for category in categories:
        number_of_services = await count_services(category.category_code)
        button_text = f"{category.category_name} ({number_of_services} шт.)"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category.category_code)
        markup.add(InlineKeyboardMarkup(text=button_text, callback_data=callback_data))
        services = await get_services(category.category_code)
        first = 1
        for service in services:
            if first == 1:
                markup.add(InlineKeyboardMarkup(text=service.name, url=service.link))
                first = 0
            else:
                markup.insert(InlineKeyboardMarkup(text=service.name, url=service.link))
    markup.row(InlineKeyboardMarkup(text="Профиль", callback_data=callback_data),
               InlineKeyboardMarkup(text="Помощь", callback_data=callback_data),
               InlineKeyboardMarkup(text="Поиск", callback_data=callback_data))
    return markup


async def services_keyboard(category):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=2)

    services = await get_services(category)

    for service in services:
        button_text = f"{service.name} - {service.short_description}"
        markup.insert(InlineKeyboardMarkup(text=button_text, url=service.link))
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           category=category,
                                           service_id=service.id)
        markup.insert(InlineKeyboardMarkup(text="Подробнее", callback_data=callback_data))
    markup.row(
        InlineKeyboardMarkup(text="Назад", callback_data=make_callback_data(level=CURRENT_LEVEL - 1)),
        InlineKeyboardMarkup(text="Поиск", callback_data=make_callback_data(level=CURRENT_LEVEL - 1))
    )
    return markup


def service_keyboard(category, service):
    CURRENT_LEVEL = 2
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardMarkup(text="Ссылка", url=service.link)
    )
    markup.row(
        InlineKeyboardMarkup(text="Назад", callback_data=make_callback_data(level=CURRENT_LEVEL - 1, category=category)),
        InlineKeyboardMarkup(text="Поиск", callback_data=make_callback_data(level=CURRENT_LEVEL - 1, category=category))
    )
    return markup
