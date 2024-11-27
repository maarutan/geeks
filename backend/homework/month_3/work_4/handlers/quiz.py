from aiogram import types, Dispatcher  # type: ignore
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # type: ignore
from config import bot
import random


async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton(text="Следующее", callback_data="quiz_2")
    keyboard.add(button)

    question = "Where are you from?"
    answer = ["Biskek", "Moscow", "Tokyo", "Tashkent"]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type="quiz",
        correct_option_id=0,
        explanation="Саткын !!!",
        open_period=60,
        reply_markup=keyboard,
    )


async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton(text="Следующее", callback_data="quiz_3")
    keyboard.add(button)

    question = "Choose a country?"
    answer = ["Kyrgyzstan", "Russia", "Japan", "Uzbekistan"]

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


async def quiz_3(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button = InlineKeyboardButton(text="Завершить", callback_data="end_quiz")
    keyboard.add(button)

    with open("./quiz/python.png", "rb") as photo:
        await call.message.answer_photo(photo=photo, caption="")

    question = "Select all correct answers:\n```print('Hello World')```"
    answer = ["Hello World", "Hello", "World", "print"]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type="quiz",
        allows_multiple_answers=True,
        correct_option_id=0,
        explanation="неправильно",
        open_period=60,
        reply_markup=keyboard,
    )


async def end_quiz(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Спасибо за участие в опросе!")


def register_quiz(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_callback_query_handler(quiz_2, text="quiz_2")
    dp.register_callback_query_handler(quiz_3, text="quiz_3")
    dp.register_callback_query_handler(end_quiz, text="end_quiz")
