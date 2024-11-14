# fsm_feg
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class fsm_registration(StatesGroup):
    fullname = State()
    email = State()
    phone_number = State()
    photo = State()


async def start_fsm(message: types.Message):
    await message.answer("Введите ваше фио: ")
    await fsm_registration.fullname.set()


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["fullname"] = message.text
    # await message.answer(f"Oтлчино!\nваше фио: {data['fullname']}")

    await fsm_registration.next()
    await message.answer("Введите ваш email: ")


async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["email"] = message.text

    # await message.answer(
    #     f"Oтлчино!\nваше фио: {data['fullname']}\nваш email: {data['email']}"
    # )
    await fsm_registration.next()
    await message.answer("Введите ваш номер телефона: ")


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone_number"] = message.text

    await message.answer(
        f"вы: {data['fullname']}\n"
        f"ваш email: {data['email']}\n"
        f"ваш номер телефона: {data['phone_number']}\n"
    )


def fsm_reg_handlers_registration(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands=["reg"], state="*")
    dp.register_message_handler(load_fullname, state=fsm_registration.fullname)
    dp.register_message_handler(load_email, state=fsm_registration.email)
    dp.register_message_handler(load_phone, state=fsm_registration.phone_number)
