from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging
import os

token = config("TOKEN")

bot = Bot(token=token)
dp = Dispatcher(bot)


button1 = InlineKeyboardButton("Кнопка 1", callback_data="remove_buttons")
button2 = InlineKeyboardButton("Кнопка 2", callback_data="remove_buttons")
button3 = InlineKeyboardButton("Кнопка 3", callback_data="remove_buttons")

# Создаём inline-клавиатуру с разными способами добавления кнопок
inline_kb = InlineKeyboardMarkup(row_width=2)  # Устанавливаем ширину строки на 2 кнопки
inline_kb.add(button1, button2)  # Добавляем две кнопки, которые будут на одной строке
inline_kb.row(button3, button1, button2)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет!", reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data == "remove_buttons")
async def remove_buttons(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=None,  # Убираем клавиатуру
    )
    await callback_query.answer("Кнопки удалены!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
    ...
