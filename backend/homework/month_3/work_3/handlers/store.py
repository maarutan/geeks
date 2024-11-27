from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


class StoreFSM(StatesGroup):
    name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    confirmation = State()


async def start_store(message: types.Message):
    await message.answer("Введите название товара:", reply_markup=ReplyKeyboardRemove())
    await StoreFSM.name.set()


async def enter_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text

    await StoreFSM.next()
    size_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    size_buttons.add("XL", "3XL", "L", "M", "S")
    await message.answer("Выберите размер:", reply_markup=size_buttons)


async def enter_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["size"] = message.text

    await StoreFSM.next()
    await message.answer(
        "Введите категорию товара:", reply_markup=ReplyKeyboardRemove()
    )


async def enter_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = message.text

    await StoreFSM.next()
    await message.answer("Введите стоимость товара:")


async def enter_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = message.text

    await StoreFSM.next()
    await message.answer("Отправьте фото товара:")


async def enter_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id

    confirmation_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    confirmation_buttons.add("Да", "Нет")

    await StoreFSM.next()
    await message.answer_photo(
        photo=data["photo"],
        caption=f'Название товара: {data["name"]}\n'
        f'Размер: {data["size"]}\n'
        f'Категория: {data["category"]}\n'
        f'Стоимость: {data["price"]}',
        reply_markup=confirmation_buttons,
    )
    await message.answer("Верные ли данные?")


async def process_confirmation(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await message.answer("Сохранено в базу", reply_markup=ReplyKeyboardRemove())
        await state.finish()
    elif message.text.lower() == "нет":
        await message.answer("Процесс отменён", reply_markup=ReplyKeyboardRemove())
        await state.finish()
    else:
        await message.answer("Пожалуйста, выберите 'Да' или 'Нет'")


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Операция отменена", reply_markup=ReplyKeyboardRemove())


def register_handlers_store(dp: Dispatcher):
    dp.register_message_handler(
        cancel_fsm, Text(equals="Cancel", ignore_case=True), state="*"
    )
    dp.register_message_handler(start_store, commands="add_item", state=None)
    dp.register_message_handler(enter_name, state=StoreFSM.name)
    dp.register_message_handler(enter_size, state=StoreFSM.size)
    dp.register_message_handler(enter_category, state=StoreFSM.category)
    dp.register_message_handler(enter_price, state=StoreFSM.price)
    dp.register_message_handler(
        enter_photo, content_types=["photo"], state=StoreFSM.photo
    )
    dp.register_message_handler(process_confirmation, state=StoreFSM.confirmation)
