from aiogram import types
from typing import List

from utils.db_api.database import db
from utils.db_api.models import Service, User


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
    if referral:
        new_user.referral = int(referral)
    await new_user.create()
    return new_user


async def add_service(**kwargs):
    new_service = await Service(**kwargs).create()
    return new_service


async def get_categories() -> List[Service]:
    return await Service.query.distinct(Service.category_code).gino.all()


async def count_services(category_code):
    return await db.select([db.func.count()]).where(
        Service.category_code == category_code).gino.scalar()


async def get_services(category_code) -> List[Service]:
    services = await Service.query.where(Service.category_code == category_code).gino.all()
    return services


async def get_service(service_id) -> Service:
    service = await Service.query.where(Service.id == service_id).gino.first()
    return service
