from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from aiogram.types import ReplyKeyboardRemove


class fsm_registration(StatesGroup):
    fullname = State()
    email = State()
    phone_number = State()
    photo = State()


async def start_fsm(message: types.Message):
    await message.answer("Введите своё фио: ", reply_markup=buttons.cancel)
    await fsm_registration.fullname.set()


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["fullname"] = message.text

    # await message.answer(f'Отлично! \n'
    #                      f'Ваше имя - {data["fullname"]}')

    await fsm_registration.next()
    await message.answer("Введи свою почту: ")


async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["email"] = message.text

    await fsm_registration.next()
    await message.answer("Введи номер телефона: ")


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["phone"] = message.text

    await fsm_registration.next()
    await message.answer("Отправь фотографию:")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id

    await state.finish()
    await message.answer_photo(
        photo=data["photo"],
        caption=f'ФИО - {data["fullname"]}\n'
        f'Почта - {data["email"]}\n'
        f'Номер телефона - {data["phone"]}',
    )


async def cance_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    kb_remove = ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer("Отменина", reply_markup=kb_remove)


def reg_handler_fsm_registration(dp: Dispatcher):
    dp.register_message_handler(
        cance_fsm, Text(equals="Cancel", ignore_case=True), state="*"
    )
    dp.register_message_handler(start_fsm, commands=["reg"])
    dp.register_message_handler(load_fullname, state=fsm_registration.fullname)
    dp.register_message_handler(load_email, state=fsm_registration.email)
    dp.register_message_handler(load_phone, state=fsm_registration.phone_number)
    dp.register_message_handler(
        load_photo, state=fsm_registration.photo, content_types=["photo"]
    )
