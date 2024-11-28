from aiogram import types, Dispatcher, Bot, executor
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = config("TOKEN")


sotrage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=sotrage)

Admins = [
    7351608256,
]
