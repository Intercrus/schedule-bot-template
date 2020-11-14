from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from states.bot_state_machine import StatesOfBot
from loader import dp, bot
from keyboards.inline.setup_keyboard import setup_inline_keyboard
from utils.misc import rate_limit
from keyboards.default.student_or_teacher_keyboard import student_or_teacher_default_keyboard


@rate_limit(limit=5)
@dp.message_handler(text="Setup")
async def setup_keyboard(message: Message):
    await message.answer(f"Choose what you want to customize",
                         reply_markup=setup_inline_keyboard)


@dp.callback_query_handler(text_contains="sub_on_schedule")
async def subscribe_to_the_schedule(call: CallbackQuery):
    await call.answer(cache_time=60)
    await bot.delete_message(message_id=call.message.message_id,
                             chat_id=call.message.chat.id)
    await StatesOfBot.schedule_state.set()


@dp.message_handler(state=StatesOfBot.schedule_state)
async def set_subscribe(message: Message, state: FSMContext):
    await state.finish()


@dp.callback_query_handler(text_contains="reset_setup", state=None)
async def reset_settings(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await bot.delete_message(message_id=call.message.message_id,
                             chat_id=call.message.chat.id)

    await call.message.answer("Settings reset successfully")
    await call.message.answer(f"Hello, {call.message.chat.full_name}!\n"
                              f"Are you a student or teacher?",
                              reply_markup=student_or_teacher_default_keyboard)

    await StatesOfBot.start_state.set()
