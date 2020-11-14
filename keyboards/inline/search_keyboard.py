from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.search_callback import search_callback

search_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Schedule for a specific day",
                             callback_data=search_callback.new(action_name="schedule_for_spec_day")),
    ],
    [
        InlineKeyboardButton(text="A specific teacher`s schedule",
                             callback_data="action:schedule_for_teacher")
    ],
    [
        InlineKeyboardButton(text="Specific group schedule",
                             callback_data="action:schedule_for_group")
    ],
])
