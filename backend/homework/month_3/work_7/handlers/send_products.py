from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from db import db_main


class EditProductFSM(StatesGroup):
    waiting_for_field = State()
    waiting_for_value = State()


async def start_edit(callback_query: types.CallbackQuery, state: FSMContext):
    product_id = int(callback_query.data.split("_")[1])
    await state.update_data(product_id=product_id)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("name_product", "size", "price", "photo", "info_product", "category")
    await callback_query.message.answer(
        "Выберите поле для редактирования:", reply_markup=keyboard
    )
    await EditProductFSM.waiting_for_field.set()


async def process_field(message: types.Message, state: FSMContext):
    field_name = message.text
    await state.update_data(field_name=field_name)
    await message.answer(f"Введите новое значение для {field_name}:")
    await EditProductFSM.waiting_for_value.set()


async def process_value(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    product_id = user_data["product_id"]
    field_name = user_data["field_name"]
    new_value = message.text

    db_main.update_product_field(product_id, field_name, new_value)
    await message.answer(f"Товар успешно обновлен: {field_name} = {new_value}")
    await state.finish()


def register_edit_handler(dp: Dispatcher):
    dp.register_callback_query_handler(start_edit, Text(startswith="edit_"), state="*")
    dp.register_message_handler(process_field, state=EditProductFSM.waiting_for_field)
    dp.register_message_handler(process_value, state=EditProductFSM.waiting_for_value)
