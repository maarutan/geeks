# commands.py
from aiogram import types, Dispatcher
from config import bot, dp
import os


async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}\n'
                                f'Твой Telegram Id - {message.from_user.id}')



async def send_mem(message: types.Message):
    # photo_path = os.path.join("media", "img.jpg")

    photo_path = "media/img.jpg"

    photo = open(photo_path, "rb")
    await message.answer_photo(photo=photo,
                               caption='Мем')
    

    # with open(photo_path, "rb") as image:
    #     await message.answer_photo(photo=image,
    #                                caption='Мем')


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(send_mem, commands=["mem"])