from aiogram.types import Message
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=10)
@dp.message_handler(text="Today")
async def schedule_today(message: Message):
    pass


@rate_limit(limit=10)
@dp.message_handler(text="Tomorrow")
async def schedule_tomorrow(message: Message):
    pass


@rate_limit(limit=30)
@dp.message_handler(text="Week")
async def schedule_for_week(message: Message):
    pass
