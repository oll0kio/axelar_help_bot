import asyncio
from asyncio import sleep

from utils.db_api.add_to_database import add_services
from utils.db_api.database import create_db


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    #from utils.notify_admins import on_startup_notify
    #await on_startup_notify(dp)
    await asyncio.sleep(5)
    await create_db()
    await asyncio.sleep(5)
    await add_services()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
