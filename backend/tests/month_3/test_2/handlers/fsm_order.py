from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from db.db_main import db
from config import bot, Admins
from aiogram.dispatcher.filters import Text
import buttons


class OrderState(StatesGroup):
    article = State()
    size = State()
    quantity = State()
    contact = State()


async def start_order(message: types.Message):
    await message.answer("Введите артикул товара:", reply_markup=buttons.cancel)
    await OrderState.article.set()


async def get_article(message: types.Message, state: FSMContext):
    await state.update_data(article=message.text)
    await message.answer("Введите размер:")
    await OrderState.size.set()


async def get_size(message: types.Message, state: FSMContext):
    await state.update_data(size=message.text)
    await message.answer("Введите количество:")
    await OrderState.quantity.set()


async def get_quantity(message: types.Message, state: FSMContext):
    await state.update_data(quantity=message.text)
    await message.answer("Введите свои контактные данные (телефон):")
    await OrderState.contact.set()


async def cancel_fsm(message: types.Message, state: FSMContext):
    if await state.get_state():
        await state.finish()
        kb_remove = types.ReplyKeyboardRemove()
        await message.reply("Операция отменена.", reply_markup=kb_remove)
    else:
        await message.reply("Нет активной операции для отмены.", reply_markup=kb_remove)


async def get_contact(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer("Ваш заказ принят! Мы скоро свяжемся с вами.")
    for admin in Admins:
        text = (
            f"Новый заказ:\n"
            f"Артикул: {data['article']}\n"
            f"Размер: {data['size']}\n"
            f"Количество: {data['quantity']}\n"
            f"Контакт: {data['contact']}"
        )
        await bot.send_message(chat_id=admin, text=text)
    await state.finish()


def register_handlers_fsm_order(dp):
    dp.register_message_handler(start_order, commands=["human"], state=None)
    dp.register_message_handler(get_article, state=OrderState.article)
    dp.register_message_handler(get_size, state=OrderState.size)
    dp.register_message_handler(get_quantity, state=OrderState.quantity)
    dp.register_message_handler(get_contact, state=OrderState.contact)
    dp.register_message_handler(
        cancel_fsm, Text(equals="cancel", ignore_case=True), state="*"
    )
