# main.py

from config import bot, dp, Admin
from aiogram import executor  # type: ignore
import logging
from handlers import command, quiz, game, fsm_reg, store, echo, fsm_store
from db import db_main


async def activeBot(_):
    for i in Admin:
        await bot.send_message(i, "Bot is Active")
        await db_main.sql_create()


async def activeisNotBot(_):
    for i in Admin:
        await bot.send_message(i, "Bot is not Active")


command.register_commands(dp)
quiz.register_quiz(dp)
game.register_game(dp)
store.register_handlers_store(dp)
fsm_store.reg_handler_fsm_store(dp)


echo.echo_register_handler(dp)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(
        dp, skip_updates=True, on_startup=activeBot, on_shutdown=activeisNotBot
    )
