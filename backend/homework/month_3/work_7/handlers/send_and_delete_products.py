from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from db import db_main
from aiogram.types import InputMediaPhoto


async def start_send_products(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_all = types.InlineKeyboardButton(
        "Вывести все товары", callback_data="all_edit_delete"
    )
    button_one = types.InlineKeyboardButton(
        "Вывести по одному", callback_data="one_edit_delete"
    )
    keyboard.add(button_all, button_one)
    await message.answer("Выберите как отправить товары:", reply_markup=keyboard)


async def send_all_products(callback_query: types.CallbackQuery):
    products = db_main.fetch_all_products()
    if products:
        for product in products:
            caption = (
                f"Заполненный товар: \n"
                f"Название - {product['name_product']}\n"
                f"Артикул - {product['product_id']}\n"
                f"Размер - {product['size']}\n"
                f"Цена - {product['price']}\n"
                f"Информация о товаре - {product['info_product']}\n"
                f"Категория - {product['category']}\n"
            )

            keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
            delete_button = types.InlineKeyboardButton(
                "Удалить", callback_data=f'delete_{product["product_id"]}'
            )
            edit_button = types.InlineKeyboardButton(
                "Редактировать", callback_data=f'edit_{product["product_id"]}'
            )
            keyboard.add(delete_button, edit_button)

            await callback_query.message.answer_photo(
                photo=product["photo"], caption=caption, reply_markup=keyboard
            )
    else:
        await callback_query.message.answer(text="В базе товаров нет!")


async def delete_product(callback_query: types.CallbackQuery):
    product_id = int(callback_query.data.split("_")[1])
    db_main.delete_product(product_id)

    if callback_query.message.photo:
        photo_404 = open("media/photo_404.png", "rb")
        await callback_query.message.edit_media(
            InputMediaPhoto(media=photo_404, caption="Товар удален. Обновите список!")
        )
    else:
        await callback_query.message.edit_text("Товар был удален. Обновите список")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(
        start_send_products, commands=["send_edit_delete_products"]
    )
    dp.register_callback_query_handler(
        send_all_products, Text(equals="all_edit_delete")
    )
    dp.register_callback_query_handler(delete_product, Text(startswith="delete_"))
