# game.py
from aiogram import types, Dispatcher  # type: ignore
from config import bot, dp
import random
from time import sleep
import asyncio


async def game_dice(message: types.Message):
    games = ["⚽", "🎰", "🏀", "🎯", "🎳", "🎲"]
    chosen_game = random.choice(games)

    await message.answer("бот: ...")
    bot_dice = await bot.send_dice(message.chat.id, emoji=chosen_game)
    bot_result = bot_dice.dice.value

    await message.answer("вы: ...")
    user_dice = await bot.send_dice(message.chat.id, emoji=chosen_game)
    user_result = user_dice.dice.value

    await asyncio.sleep(5)
    if bot_result > user_result:
        await message.answer("Бот выиграл!")
    elif bot_result < user_result:
        await message.answer("Вы выиграли!")
    else:
        await message.answer("Ничья!")


def register_game(dp: Dispatcher):
    dp.register_message_handler(game_dice, commands=["game"])
