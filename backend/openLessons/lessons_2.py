# TODO:  alt + shift + r start code
# TODO: ctrl + t terminalhello world

import random

random_box = ["камень", "ножницы", "бумага"]

user = input("Введите камень, ножницы или бумага")

bot = random.choice(random_box)

if bot == user:
    print(f"Бот выбрал: {bot} Я выбрал {user} Ничья")

elif (
    bot == "камень"
    and user == "ножницы"
    or bot == "ножницы"
    and user == "бумага"
    or bot == "бумага"
    and user == "камень"
):
    print(f"Бот выбрал: {bot} Я выбрал {user} Бот выйграл")

elif (
    user == "камень"
    and bot == "ножницы"
    or user == "ножницы"
    and bot == "бумага"
    or user == "бумага"
    and bot == "камень"
):
    print(f"Бот выбрал: {bot} Я выбрал {user} Я выйграл")
else:
    print("Нет таких фигур")
