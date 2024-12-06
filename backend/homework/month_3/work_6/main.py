from config import bot, dp, Admins
from aiogram import executor, types
import logging
from handlers import (
    command,
    quiz,
    fsm_reg,
    echo,
    fsm_store,
    send_products,
    send_and_delete_products,
)
from db import db_main


async def on_startup(_):
    db_main.sql_create()  # Убрано "await", так как sql_create синхронная
    for admin in Admins:
        await bot.send_message(chat_id=admin, text="Бот включен!")


async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text="Бот выключен!")


command.register_commands(dp)
quiz.register_handler_quiz(dp)
fsm_reg.reg_handler_fsm_registration(dp)
fsm_store.reg_handler_fsm_store(dp)

send_products.register_handlers(dp)
send_and_delete_products.register_handlers(dp)

echo.register_echo(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(
        dp,
        skip_updates=True,
        allowed_updates=["callback"],
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
