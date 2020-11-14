from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from aiogram.dispatcher import FSMContext
from states.bot_state_machine import StatesOfBot
from keyboards.default.student_or_teacher_keyboard import student_or_teacher_default_keyboard
from utils.db_api import quick_commands as commands


@dp.message_handler(CommandStart(), state=None)
async def command_start(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    await commands.add_user(id=message.from_user.id,  # Add to the database
                            name=name)

    await message.answer(f"Hello, {message.from_user.full_name}!\n"
                         f"Are you a student or teacher?",
                         reply_markup=student_or_teacher_default_keyboard)

    await StatesOfBot.start_state.set()
