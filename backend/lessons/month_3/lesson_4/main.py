import logging
from aiogram import executor  
from config import Admin, bot, dp
from handlers import command, echo, fsm_reg, quiz



async def on_startup(_):
    for admin in Admin:
        await bot.send_message(admin, "Бот запущен")


async def off_startup(_):
    for admin in Admin:
        await bot.send_message(admin, "Бот завершил запуск")


command.register_commands(dp)
quiz.register_quiz(dp)
fsm_reg.reg_handler_fsm_registration(dp)

echo.register_echo(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(
        dp, skip_updates=True, on_startup=on_startup, on_shutdown=off_startup
    )
