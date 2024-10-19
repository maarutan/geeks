"""
Урок 1. Тема №1. Базовый синтаксис, переменные, комментарии, встроенные функции. Типы данных(базовые): строки, целые и дробные числа. Арифметические операторы.
"""

import os

# a = 8
# b = 4

# result = b % a
# print(result)


# str - строка тип данных в Python
# int - инт является целым числом
# floot - дробное число


# name = "marat"  # str
# age = "16"  # str
# hgiht = 1.85  # float

# formmater - форматирование строк
# f'' - f-string
# {name} - подставляет значение переменной name

# print("-" * 20)
# print(f"my name is {name}\nmy age is {age}\nmy hgiht is {hgiht}")
# print("-" * 20)
try:
    week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    totalSum = 0

    for day in week:
        os.system("clear")
        userInput = float(input(f"{day} - потрачено: "))
        totalSum += userInput

    totalWeek = len(week)
    total = totalSum / totalWeek
    total = round(total, 1)

    if total % 1 == 0:
        total = int(total)

    if totalSum % 1 == 0:
        totalSum = int(totalSum)

    print("\nResult:")
    print("-" * 40)
    print(f"\nВсего потрачено за неделю: {totalSum} som")
    print(f"Среднее потрачено в день: {total} som")
except KeyboardInterrupt:
    print(
        """           \n
 _
| |__ _  _ ___   
| '_ \ || / -_) 
|_.__/\_, \___| 
      |__/      
          """
        + "     "
        + """/)＿/)☆
             ／(๑^᎑^๑)っ ＼
            |￣∪￣  ￣|＼／
            |＿＿_＿＿|／

          
          """
    )
