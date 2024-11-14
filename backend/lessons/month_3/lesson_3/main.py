from config import bot, dp
from aiogram import Bot, Dispatcher, executor, types  # type: ignore
import logging
from handlers import command, quiz, fsm_reg

command.register_commands(dp)
quiz.register_quiz(dp)
fsm_reg.fsm_reg_handlers_registration(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
