from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

student_or_teacher_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Student"),
            KeyboardButton(text="Teacher")
        ]
    ],
    resize_keyboard=True
)
