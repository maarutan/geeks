from aiogram import Bot, Dispatcher
from decouple import Config, RepositoryEnv
from aiogram.contrib.fsm_storage.memory import MemoryStorage

Admins = [
    7351608256,
]

config = Config(RepositoryEnv("../env"))
token = config("TOKEN1")
bot = Bot(token=token)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
