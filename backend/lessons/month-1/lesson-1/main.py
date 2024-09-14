# Базовый синтаксис, переменные, коменнтарии, встроинные функции.
# Типы данных(базовые): строки, целые и дробные числа. Aрифметические операторы.

# str = strining
# int = integer
# float = floating


# name = "samat"
# surname = "abdrahmanov"
# age = 21
# hight = 1.78


# print(type(name)) # <calss 'str'>
# print(type(age)) # <class 'int'>
# print(type(hight)) # <class 'float'>


# зачем нужны разные ковычки???
# " "
# ' '
# чтобы python понял что это строка нужно использовать ' ' & " "
# например   name = "samat" но если например  word = "i"m" <== этот текст в python поддерживаться не булет будет конфликт и это плохо как првильно ???
# word = "i'm"
# также можно использовать \ \ чтобы убрать конфликт например
# word = "i\"am\""    но согласитесь это не удобно ^^
# в таком случье python читает текст и конфликта межну ковычками нет !


# разберем функцую type() --- что она делает она выводит тип а тоесть класс или тип чего либо  например  print(type(name))
# в логе выйдет  <class 'str'>   что означает это string  а тоесть строка


# функция title()
# она делает первую букву за главной а то есть  name = "marat".title()о в логах выйдет  "Marat"

# функция upper() она итерпиритирует слово на верхний регистер  lower() это уже нижний регистер


# типы форматов строки тоесть вывода
# ---------------------------------------------
# print(f'name: {name} surname: {surname}')
# print("name:", name, "surname:", surname)
# print("name:", name, "surname: ", surname, "age ", age)
# print('name: ' + name + 'surname: ' + surname)
# print('name: ', name, 'surname: ', surname)
# print('name: {} surname: {} '.format(name, surname))


# как можно ставить переменные : true

# good = 5
# good_one = 5
# good_1 = 5
# goodOne = 5
# Good = 4
# GOOD = 4

# как нельзя ставить переменные : false
# 123bad = 0
# (*!>/?bad = 0
# for = 0
# while = 0
# in = 0

# Арифмитичкие операторы.


# print(5 + 5)  # плюс
# print(5 - 5)  # минус
# # тут приоритет будет выше

# print(2 + 3 * 5)  # в скобках
# print((2 + 3) * 5)  # в скобках

# print(5 * 5)  # умножение
# print(20 % 8)  # остаток
# print(5 / 5)  # делениеou
# print(5 // 5)  # деление без остатка
# print(2 ** 5)  # возвидение в степень


# фунция int() позволяет типизировать в число


# name = input(f'Enter your name : ')
# age = int(input(f'Enter your age :'))
# current_year = 2024
# born = current_year - age

# print(f'{name}, age: {age} in the world {born} year')


# total_sum_ages = 14 + 17 + 17 + 18 + 15 + 15 + 15 + 15 + 13 + 18 + 16 + 13 + 15 + 16 + 18 + 16 + 16 + 16 + 30 + 45 + 20

# stud_count = 21
# averageAge = total_sum_ages / stud_count
# averageAge = round(averageAge,2)
# print(f'total age this group:',averageAge)

# фунция round() это функция позволяет округлить остаток
