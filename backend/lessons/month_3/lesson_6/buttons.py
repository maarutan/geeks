# buttons.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a = False
cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=a)
cancel_button = KeyboardButton("Отмена")
cancel.add(cancel_button)

size = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=a, row_width=2)
size.add(
    KeyboardButton("S"), KeyboardButton("M"), KeyboardButton("L"), KeyboardButton("XL")
)

submit = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=a, row_width=1)
submit.add(KeyboardButton("Да"), KeyboardButton("Нет"))
