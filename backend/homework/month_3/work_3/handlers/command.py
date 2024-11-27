# command.py
from aiogram import types, Dispatcher  # type: ignore
from config import bot, dp
import os
import random


# @dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Hello! {message.from_user.first_name}\n"
        f"your Telegram id = {message.from_user.id}",
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"че как дела у вас {message.from_user.first_name}\n",
    )


async def send_mem(message: types.Message):
    photoPath = os.path.join("./media", random.choice(os.listdir("./media")))
    with open(photoPath, "rb") as photo:
        await message.answer_photo(photo=photo, caption="/mem")


# with open(photoPath, "rb") as photo:


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(send_mem, commands=["mem"])
