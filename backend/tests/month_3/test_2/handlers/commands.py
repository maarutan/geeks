from aiogram import types, Dispatcher


async def start(message: types.Message):
    with open("img/image.png", "rb") as photo:
        await message.reply_photo(
            photo,
            caption=f"Привет, {message.from_user.first_name}\nДобро Пожаловать в Магазинe Марата",
        )


async def info(message: types.Message):
    await message.reply(
        "Информация:\n"
        f"текуший пользователь: {message.from_user.first_name}\n"
        f"текуший юзер: {message.from_user.id}\n"
        f"версия бота: 1.0\n"
        f"бот для Интернет магазина Марата\n"
        f"все права защищены © 2024\n"
        f"{'-'*50}\n"
        f"консультация: @maarutan\n"
        f"tg: @maarutan\n"
        f"email: maratarzymatov288@gmail.com\n"
        f"phone: +996 999 99-99-99\n"
    )


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(info, commands=["info"])
