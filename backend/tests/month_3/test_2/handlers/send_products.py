# send_products.py

from aiogram.dispatcher.filters import Text
import buttons
from aiogram import types
from db.db_main import db


async def send_products(message: types.Message):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM store")
    products = cursor.fetchall()

    if not products:
        await message.answer("Товары пока не добавлены.")
        return

    for product in products:
        product_text = (
            f"Название: {product[1]}\n"
            f"Размер: {product[2]}\n"
            f"Цена: {product[3]} c\n"
        )
        if product[4]:
            await message.answer_photo(photo=product[4], caption=product_text)
        else:
            await message.answer(product_text)


def register_handlers_send_products(dp):
    dp.register_message_handler(send_products, commands=["prod"])
