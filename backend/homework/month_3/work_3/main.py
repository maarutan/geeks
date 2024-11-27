from config import bot, dp
from aiogram import executor  # type: ignore
import logging
from handlers import command, quiz, game, fsm_reg, store

command.register_commands(dp)
quiz.register_quiz(dp)
game.register_game(dp)
# fsm_reg.reg_handler_fsm_store(dp)
store.register_handlers_store(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
