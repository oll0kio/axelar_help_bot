from aiogram import types

from utils.db_api.database import db
from utils.db_api.models import User


async def get_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def get_user_by_id(id):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def add_new_user(referral=None):
    user = types.User.get_current()
    old_user = await get_user(user.id)
    if old_user:
        return old_user
    new_user = User()
    new_user.user_id = user.id
    new_user.username = user.username
    new_user.full_name = user.full_name
    await new_user.create()
    return new_user

async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total
