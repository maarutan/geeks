from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class fsm_registration(StatesGroup):
    fullname = State()
    email = State()
    username = State()
    phone = State()
    photo = State()


async def start(message: types.Message, state: FSMContext):
    await message.answer("Введите ФИО")
    await fsm_registration.fullname.set()

async def load_fullname(message: types.Message, state: FSMContext)
    await with 812
