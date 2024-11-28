# fsm_store.py

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from db import db_main
import buttons


class FSMStore(StatesGroup):
    name_product = State()
    id_product = State()
    size = State()
    price = State()
    photo = State()
    submit = State()


async def start_fsm(message: types.Message, state: FSMContext):
    await FSMStore.name_product.set()
    await message.answer(
        "Введи название продукта: ",
        reply_markup=buttons.cancel,
    )


async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name_product"] = message.text

    await message.answer("введите арьтикул продукта: ")
    await FSMStore.next()


async def load_products_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["id_product"] = message.text

    await message.answer("введите размер: ", reply_markup=buttons.size)
    await FSMStore.next()


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["size"] = message.text

    await message.answer("введите цену: ", reply_markup=buttons.cancel)
    await FSMStore.next()


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = message.text

    await message.answer("отправьте фото товара: ", reply_markup=buttons.cancel)
    await FSMStore.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id

    await message.reply_photo(
        photo=data["photo"],
        caption=f"Вы добавили товар:\n"
        f"название - {data['name_product']}\n"
        f"артикул - {data['id_product']}\n"
        f"размер - {data['size']}\n"
        f"цена - {data['price']}\n",
        reply_markup=buttons.cancel,
    )
    await FSMStore.next()
    await message.answer("Сохранить?", reply_markup=buttons.submit)


kb_remove = types.ReplyKeyboardRemove()


async def submit(message: types.Message, state: FSMContext):
    if message.text == "Да":
        await message.answer("Товар сохранен", reply_markup=kb_remove)
    else:
        await message.answer("Товар не сохранен\nПопробуйте еще раз\n\nвведите да/нет")
        # await db_main
    async with state.proxy() as data:
        await db_main.insert_store(
            name_product=data["name_product"],
            size=data["size"],
            price=data["price"],
            photo=data["photo"],
        )
    await state.finish()


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    await message.answer("Отменено!", reply_markup=kb_remove)


def register_handlers_fsm_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands="fsm_store", state=None)
    dp.register_message_handler(load_name_product, state=FSMStore.name_product)
    dp.register_message_handler(load_products_id, state=FSMStore.id_product)
    dp.register_message_handler(load_size, state=FSMStore.size)
    dp.register_message_handler(load_price, state=FSMStore.price)
    dp.register_message_handler(
        load_photo, state=FSMStore.photo, content_types=["photo"]
    )
    dp.register_message_handler(submit, state=FSMStore.submit)
    dp.register_message_handler(
        cancel, Text(equals="отмена", ignore_case=True), state="*"
    )
