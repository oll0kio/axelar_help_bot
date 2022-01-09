import asyncio

from gino import Gino
from gino.schema import GinoSchemaVisitor
from data.config import POSTGRES_URI
from utils.db_api.add_to_database import add_services

db = Gino()


# Документация
# http://gino.fantix.pro/en/latest/tutorials/tutorial.html

async def create_db():
    # Устанавливаем связь с базой данных
    await db.set_bind(POSTGRES_URI)
    db.gino: GinoSchemaVisitor
    await db.gino.create_all()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(create_db())
    loop.run_until_complete(add_services())
