# buttons.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a = False
cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=a)
cancel_button = KeyboardButton('Отмена')
cancel.add(cancel_button)


submit = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2).add(KeyboardButton('Да'), KeyboardButton('Нет'))

# submit = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
# submit.add(cancel_button)