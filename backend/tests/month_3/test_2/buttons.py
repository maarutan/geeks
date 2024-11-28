from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
cancel_button = KeyboardButton("cancel")
cancel.add(cancel_button)

size = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
size_XL = KeyboardButton("XL")
size_L = KeyboardButton("L")
size_M = KeyboardButton("M")
size.add(size_XL, size_L, size_M)

submit = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
submit_button = KeyboardButton("submit")
submit.add(submit_button, cancel_button)
