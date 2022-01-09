from gino import Gino
from gino.schema import GinoSchemaVisitor
from data.config import DB_USER, DB_PASS, DB_HOST, DB_NAME

db = Gino()


async def create_db():
    await db.set_bind(f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')

    # Create tables
    db.gino: GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()