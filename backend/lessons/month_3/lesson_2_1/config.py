from aiogram import Bot, Dispatcher  # type: ignore
from decouple import Config, RepositoryEnv  # type: ignore
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
config = Config(RepositoryEnv("../.env"))
token = config("TOKEN1")
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)
