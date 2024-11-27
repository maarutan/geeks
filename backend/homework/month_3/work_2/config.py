from aiogram import Bot, Dispatcher  # type: ignore
from decouple import config  # type: ignore


token = config("TOKEN2")
bot = Bot(token=token)
dp = Dispatcher(bot)
