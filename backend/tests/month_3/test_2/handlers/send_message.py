from aiogram import types, Dispatcher


async def echo_message(message: types.Message):
    await message.reply(message.text)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(echo_message)
