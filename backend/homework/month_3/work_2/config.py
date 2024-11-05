from aiogram import Bot, Dispatcher  # type: ignore
from decouple import Config, RepositoryEnv  # type: ignore


config = Config(RepositoryEnv("../.env"))
token = config("TOKEN")
bot = Bot(token=token)
dp = Dispatcher(bot)
