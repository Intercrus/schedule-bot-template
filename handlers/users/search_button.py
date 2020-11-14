from aiogram.types import Message, CallbackQuery
from loader import dp, bot
from keyboards.inline.search_keyboard import search_inline_keyboard
from aiogram.dispatcher import FSMContext
from states.bot_state_machine import StatesOfBot


@dp.message_handler(text="Search")
async def search_button(message: Message):
    await message.answer(f"Choose what you want to find",
                         reply_markup=search_inline_keyboard)


@dp.callback_query_handler(text_contains="schedule_for_spec_day")
async def schedule_for_a_specific_day(call: CallbackQuery):
    await call.answer(cache_time=60)
    await bot.delete_message(message_id=call.message.message_id,
                             chat_id=call.message.chat.id)
    await StatesOfBot.search_by_spec_day.set()


@dp.message_handler(state=StatesOfBot.search_by_spec_day)
async def search_timetable_by_specific_day(message: Message, state: FSMContext):
    await state.finish()


@dp.callback_query_handler(text_contains="schedule_for_teacher")
async def specific_teachers_schedule(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await bot.delete_message(message_id=call.message.message_id,
                             chat_id=call.message.chat.id)
    await StatesOfBot.search_by_teacher_state.set()


@dp.message_handler(state=StatesOfBot.search_by_teacher_state)
async def search_timetable_by_specific_teacher(message: Message, state: FSMContext):
    await state.finish()


@dp.callback_query_handler(text_contains="schedule_for_group")
async def specific_group_day(call: CallbackQuery):
    await call.answer(cache_time=60)
    await bot.delete_message(message_id=call.message.message_id,
                             chat_id=call.message.chat.id)
    await StatesOfBot.search_by_name_group.set()


@dp.message_handler(state=StatesOfBot.search_by_name_group)
async def search_timetable_by_specific_name_group(message: Message, state: FSMContext):
    await state.finish()
