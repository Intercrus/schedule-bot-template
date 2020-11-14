from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(id: int, name: str):
    try:
        user = User(id=id, name=name)
        await user.create()

    except UniqueViolationError:  # if two unique keys
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user
