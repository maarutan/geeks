from aiogram import Bot, Dispatcher  # type: ignore
from decouple import Config, RepositoryEnv  # type: ignore
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # type: ignore

Admin = [
    7351608256,
]


config = Config(RepositoryEnv("../.env"))
token = config("TOKEN1")
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
