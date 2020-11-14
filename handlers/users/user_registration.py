from keyboards.default.main_menu import main_menu_default_keyboard
from loader import dp
from aiogram.dispatcher import FSMContext
from states.bot_state_machine import StatesOfBot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types


@dp.message_handler(state=StatesOfBot.start_state, text="Student")
async def pressed_button_student(message: types.Message, state: FSMContext):
    await message.answer(f'Enter your class/group name\n',
                         reply_markup=ReplyKeyboardRemove())

    await StatesOfBot.enter_student.set()


@dp.message_handler(state=StatesOfBot.start_state, text="Teacher")
async def pressed_button_teacher(message: types.Message, state: FSMContext):
    await message.answer(f'Enter you name\n', reply_markup=ReplyKeyboardRemove())

    await StatesOfBot.enter_teacher.set()


@dp.message_handler(state=StatesOfBot.enter_student)
async def search_groups(message: Message, state: FSMContext):
    await message.answer(f"Group {message.text} found successfully.\n"
                         f"Select the button you are interested in",
                         reply_markup=main_menu_default_keyboard)
    await state.finish()


@dp.message_handler(state=StatesOfBot.enter_teacher)
async def search_groups(message: Message, state: FSMContext):
    await message.answer(f"Teacher {message.text} found successfully.\n"
                         f"Select the button you are interested in",
                         reply_markup=main_menu_default_keyboard)
    await state.finish()
