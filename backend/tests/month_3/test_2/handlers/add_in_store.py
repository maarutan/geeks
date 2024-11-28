from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from config import Admins
from db import db_main
import buttons

kb_remove = types.ReplyKeyboardRemove()


class RegisterFSM(StatesGroup):
    name = State()
    category = State()
    size = State()
    articul = State()
    photo = State()


async def add_in_store(message: types.Message):
    if message.from_user.id in Admins:
        await RegisterFSM.name.set()
        await message.reply("Введите название товара: ", reply_markup=buttons.cancel)
    else:
        await message.reply("Вы не администратор!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await RegisterFSM.next()
    await message.reply("Введите категорию: ")


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = message.text
    await RegisterFSM.next()
    await message.reply("Введите размер: ")
    await message.answer("Выберите размер:", reply_markup=buttons.size)


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["size"] = message.text
    await RegisterFSM.next()
    await message.reply("Введите артикул: ", reply_markup=buttons.cancel)


async def load_articul(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply("Артикул должен содержать только цифры. Попробуйте снова.")
        return
    async with state.proxy() as data:
        data["articul"] = message.text
    await RegisterFSM.next()
    await message.reply("Отправьте фото: ")


async def load_photo(message: types.Message, state: FSMContext):
    if not message.photo:
        await message.reply("Пожалуйста, отправьте фото!")
        return

    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id
        await message.reply_photo(
            data["photo"],
            caption=(
                f"Товар: {data['name']}\n"
                f"{'-'*50}\n"
                f"Категория: {data['category']}\n"
                f"Размер: {data['size']}\n"
                f"Артикул: {data['articul']}\n"
                f"{'-'*50}\n"
                f"Админ: {message.from_user.first_name} ^^\n"
                f"Все права защищены © 2024"
            ),
        )
        await message.reply("сохранить в базу ?", reply_markup=buttons.submit)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "submit":
        async with state.proxy() as data:
            await db_main.insert_store(
                data["name"],
                data["category"],
                data["size"],
                data["articul"],
                data["photo"],
            )
        await message.reply("Товар успешно добавлен!", reply_markup=kb_remove)
    elif message.text.lower() == "cancel":
        await message.reply("Добавление товара отменено.", reply_markup=kb_remove)
    else:
        await message.reply(
            "Неверная команда. Попробуйте снова.", reply_markup=kb_remove
        )
    await state.finish()


async def cancel_fsm(message: types.Message, state: FSMContext):
    if await state.get_state():
        await state.finish()
        kb_remove = types.ReplyKeyboardRemove()
        await message.reply("Операция отменена.", reply_markup=kb_remove)
    else:
        await message.reply("Нет активной операции для отмены.", reply_markup=kb_remove)


def register_fsm_add(dp: Dispatcher):
    dp.register_message_handler(add_in_store, commands=["add"])
    dp.register_message_handler(
        cancel_fsm, Text(equals="cancel", ignore_case=True), state="*"
    )
    dp.register_message_handler(load_name, state=RegisterFSM.name)
    dp.register_message_handler(load_category, state=RegisterFSM.category)
    dp.register_message_handler(load_size, state=RegisterFSM.size)
    dp.register_message_handler(load_articul, state=RegisterFSM.articul)
    dp.register_message_handler(submit, Text(equals="submit", ignore_case=True))
    dp.register_message_handler(
        submit,
        Text(equals=["submit", "cancel"], ignore_case=True),
        state=RegisterFSM.photo,
    )
    dp.register_message_handler(
        load_photo, content_types=["photo"], state=RegisterFSM.photo
    )
