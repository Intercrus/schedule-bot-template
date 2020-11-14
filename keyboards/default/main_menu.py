from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Today"),
            KeyboardButton(text="Tomorrow")
        ],
[
            KeyboardButton(text="Week"),
        ],
        [
            KeyboardButton(text="Search"),
        ],
        [
            KeyboardButton(text="Setup")
        ]
    ],
    resize_keyboard=True
)
