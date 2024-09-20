"""Фунция аргументом, параметры, виды аргументов """
# DRY - don't repeat youself

"""Схема Фунции"""


def getData(name, surname="неизвестно"):
    print(f"ваша имя: {name} ваша фамилия: {surname}")


getData("marat", "arzyamtov")  # фунция с вводом аргумента
# фунция с вводом ключивых параметров с аргументом
getData(name="leo", surname="alexandro")

getData("marat")  # фунция с вводом аргумента


# lengh = 25
# width = 5
# square = lengh * width

# print(square)

# lengh = 25
# width = 5
# square_3 = lengh * width

# print(square_3)
