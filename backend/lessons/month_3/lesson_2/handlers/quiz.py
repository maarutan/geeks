# quiz.py
from aiogram import types, Dispatcher  # type: ignore
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # type: ignore
from config import bot


async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton(text="Cледующее", callback_data="quiz_2")
    keyboard.add(button)

    question = "where are you from ?"
    answer = ["Biskek", "Moscow", "Tokyo", "Tashkent"]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type="quiz",
        correct_option_id=0,
        explanation="Эмигрант",
        open_period=60,
        reply_markup=keyboard,
    )


async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton(text="Cледующее", callback_data="quiz_2")
    keyboard.add(button)

    question = "Chosise country ?"
    answer = ["Kygyzstan", "Russian", "Japan", "Uzbekistan"]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type="quiz",
        correct_option_id=0,
        explanation="Эмигрант",
        open_period=60,
        reply_markup=keyboard,
    )


def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, text="quiz_2")
