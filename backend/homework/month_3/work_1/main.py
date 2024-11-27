from decouple import Config, RepositoryEnv  # type: ignore
from aiogram import Bot, Dispatcher, executor, types  # type: ignore
import logging


config = Config(RepositoryEnv("../.env"))
token = config("TOKEN2")
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Hello! {message.from_user.first_name}\n"
        f"your Telegram id = {message.from_user.id}",
    )

    await message.answer("Hello! I'm a bot")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
