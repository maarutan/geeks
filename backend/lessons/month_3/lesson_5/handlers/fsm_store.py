from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from db import db_main


class store_fsm(StatesGroup):
    name_product = State()
    product_id = State()
    size = State()
    price = State()
    photo = State()
