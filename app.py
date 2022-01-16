import asyncio

from aiogram import executor

from utils.db_api.database import create_db
from loader import bot


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    # Подождем пока запустится база данных...
    await asyncio.sleep(5)
    await create_db()


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)