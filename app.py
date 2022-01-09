import asyncio

from aiogram import executor

from utils.db_api.database import create_db
from utils.db_api.add_to_database import add_services
from loader import bot


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    # Подождем пока запустится база данных...
    await asyncio.sleep(5)
    await create_db()
    await asyncio.sleep(5)
    await add_services()


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)