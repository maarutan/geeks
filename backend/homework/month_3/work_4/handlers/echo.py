from aiogram import types, Dispatcher
from time import sleep


async def echo_message(message: types.Message):
    if message.text.isdigit():
        try:
            result = int(message.text) ** 2
            await message.answer(result)
        except ValueError:
            await message.answer("ввидите число или слово")
    else:
        await message.answer(message.text)


def echo_register_handler(dp: Dispatcher):
    dp.register_message_handler(echo_message)
