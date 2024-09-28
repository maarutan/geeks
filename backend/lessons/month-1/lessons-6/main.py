"""Фунция аргументом, параметры, виды аргументов """
# DRY - don't repeat youself

"""Схема Фунции"""

# def getData(name, surname="неизвестно"):
#     print(f"ваша имя: {name} ваша фамилия: {surname}")


# getData("marat", "arzyamtov")  # фунция с вводом аргумента
# # фунция с вводом ключивых параметров с аргументом
# getData(name="leo", surname="alexandro")

# getData("marat")  # фунция с вводом аргумента


# lengh = 25
# width = 5
# square = lengh * width

# print(square)

# lengh = 25
# width = 5
# square_3 = lengh * width

# print(square_3)


# def getSquare(lengh: int, width: int) -> int:
#     """ Принимает ширину и длину и возращяет перимтр"""
#     return lengh * width


# suquare = getSquare(8, 4)

# print(getSquare(25, 10))
# print(suquare)


# print(help(len))
# print(len.__doc__)

# def summing(*args): #args это кортеж
#     return sum(args)

# print(summing(22, 54, 23))

# def maxi(*args: int) -> int:
#     """maximaze number"""
#     return int(max(args))
# print(maxi("hello"))

# def menu(**kwargs):
#     return kwargs

# mon = menu(eat='burger', dring='cola')
# print(mon)

"""
4 вида параметров фунции 
--------------------------|
1 - обезательно позиционный
2 - не обезательно позиционный
3 - * -args
4 - ** -kwargs
"""

# from pprint import pprint
# expenses = 0
# days = 7
# data = {}

# for day in range(1, days+1):
#     inputExpens = int(input(f'day:({day}) enter expensess: '))
#     expenses += inputExpens
#     data[day] = inputExpens

# pprint(data, width=1)


data = tuple(map(int, input("enter expenssion: ").split()))
print(data)
print(sum(data))
print(round(sum(data) / len(data), 1))
