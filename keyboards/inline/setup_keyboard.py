from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.setup_callback import setup_callback

setup_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Subscribe to the schedule",
                             callback_data=setup_callback.new(action_name="sub_on_schedule")),
    ],
    [
        InlineKeyboardButton(text="Reset settings",
                             callback_data="action:reset_setup")
    ]
])
