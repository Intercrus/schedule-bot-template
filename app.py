from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    print("Connect db")
    await db_gino.on_startup(dp)
    print("Complete")

    print("Create tables")
    await db.gino.create_all()

    print("Complete")
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
