from config import bot, dp
from aiogram import Bot, Dispatcher, executor, types  # type: ignore
import logging
from handlers import command, quiz

command.register_commands(dp)
quiz.register_quiz(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
