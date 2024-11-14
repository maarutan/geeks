from config import bot, dp, Admin
from aiogram import executor  # type: ignore
import logging
from handlers import command, quiz, fsm_reg, echo


async def on_startup(_):
    for admin in Admin:
        await bot.send_message(admin, "Бот запущен")


command.register_commands(dp)
quiz.register_quiz(dp)
fsm_reg.reg_handler_fsm_registration(dp)

echo.register_echo(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
