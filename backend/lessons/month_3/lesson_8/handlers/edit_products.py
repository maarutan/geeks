# edit_products.py
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import db_main


class edit_products_fsm(StatesGroup):
    for_field = State()
    for_new_field = State()
    for_photo = State()


async def start_send_products(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_all = InlineKeyboardButton('Вывести все товары', callback_data='all_edit')
    button_one = InlineKeyboardButton('Вывести по одному товару', callback_data='one_edit')
    keyboard.add(button_all, button_one)

    await message.answer(text='Выберите как отправить твары:', reply_markup=keyboard)



async def send_all_products(callback_query: types.CallbackQuery):
    products = db_main.fetch_all_products()
    if products:
        for product in products:
            caption = (f"Заполненный товар: \n"
                       f"Название - {product['name_product']}\n"
                       f"Артикул - {product['product_id']}\n"
                       f"Размер - {product['size']}\n"
                       f"Цена - {product['price']}\n"
                       f"Информация о товаре - {product['info_product']}\n"
                       f"Категория - {product['category']}\n")
            
            edit_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
            edit_keyboard.add(InlineKeyboardButton('Редактировать', 
                                                   callback_data=f'edit_{product["product_id"]}'))

            await callback_query.message.answer_photo(
                photo=product['photo'],
                caption=caption,
                reply_markup=edit_keyboard
            )
    else:
        await callback_query.message.answer(text='В базе товаров нет!')


async def edit_product(call: types.CallbackQuery, state: FSMContext):
    product_id = call.data.split('_')[1]

    await state.update_data(product_id=product_id)

    keyboard = InlineKeyboardMarkup(row_width=2)

    name_button = InlineKeyboardButton(text="Название", callback_data="field_name_product")
    category_button = InlineKeyboardButton(text="Категория", callback_data="field_category")
    price_button = InlineKeyboardButton(text="Цена", callback_data="field_price")
    size_button = InlineKeyboardButton(text="Размер", callback_data="field_size")
    photo_button = InlineKeyboardButton(text="Фото", callback_data="field_photo")
    info_button = InlineKeyboardButton(text="Инфо о товаре", callback_data="field_info_product")

    keyboard.add(name_button, category_button, price_button, size_button, photo_button, info_button)

    await call.message.answer(text='Выберите поле для редактирования:', reply_markup=keyboard)

    await edit_products_fsm.for_field.set()


async def select_field_product(call: types.CallbackQuery, state: FSMContext):
    field_map = {
        "field_name_product": "name_product",
        "field_category": "category",
        "field_price": "price",
        "field_size": "size",
        "field_photo": "photo",
        "field_info_product": "info_product"
    }

    field = field_map.get(call.data)

    if not field:
        await call.message.answer('Недопустимое поле!')
        return
    
    await state.update_data(field=field)

    if field == 'photo':
        await call.message.answer("Отправьте новое фото:")
        await edit_products_fsm.for_photo.set()
    else:
        await call.message.answer('Отправьте новое значение: ')
        await edit_products_fsm.for_new_field.set()

async def set_new_value(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    product_id = user_data['product_id']

    field = user_data['field']

    new_value = message.text

    db_main.update_product_field(product_id, field, new_value)

    await message.answer(f'Поле {field} успешно обновлено!')
    await state.finish()

async def set_new_photo(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    product_id = user_data['product_id']

    photo_id = message.photo[-1].file_id

    db_main.update_product_field(product_id, 'photo', photo_id)

    await message.answer('Фото успешно обновлено!')
    await state.finish()


def register_edit_handler(dp: Dispatcher):
    dp.register_message_handler(start_send_products, commands=['edit_product'])
    dp.register_callback_query_handler(send_all_products, Text(equals='all_edit'))
    dp.register_callback_query_handler(edit_product, Text(startswith='edit_'), state='*')
    dp.register_callback_query_handler(select_field_product, Text(startswith='field_'), 
                                       state=edit_products_fsm.for_field)
    dp.register_message_handler(set_new_value, state=edit_products_fsm.for_new_field)
    dp.register_message_handler(set_new_photo, state=edit_products_fsm.for_photo, 
                                content_types=['photo'])