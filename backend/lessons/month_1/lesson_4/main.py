"""Списки, кортежи.  Индексы и срезы. Встроенные функции к наборам элементов. Списковое включение List comprehension.
"""

"""Встроенные функции к наборам элементов."""

# number = [11, 23, 45, 67, 89, 90, 11]

# totalcound = 0
# for i in number:
#     totalcound += 1
# print(number)
# print(totalcound)


# print(len(number))  # вычисляет длину числа
# print(min(number)) # вычисляет минимальное число
# print(man(number)) # вычисляет максимальное число
# print(sum(number)) # апсолутное сложение
# print(any(number)) # возвращяет true если что либо вообще есть
# print(all(number)) # возвращяет true если все true так же возвращает false если хоть 1 false


"""Кортеж"""

# numbes = (34, 67, 12, 46, 59, 87, 92)  # Кортеж turple()


# """
# методы кортежа это

# cound - метод который проверят количесво схожих чисел
# """


# print(numbes)
# print(type(numbes))  # <class 'tuple' > Кортеж

"""лист"""

#  [] это листе его тип <class 'list'>
# students = ["bilal", "dair", "aidana", "ulan", "bilal"]
# students = tuple(students)
# print(students)
# print(students.index("bilal", 2))


# newStudents = students.copy()  # мы копируем students чтобы он не ссылался
# # newStudents[0] = "marat"


# print(students)
# print(newStudents)

# print(id(students))  # каждый обк несет уникальный id
# print(id(newStudents))  # каждый обк несет уникальный id

# print(students == newStudents)  # true
# print(students is newStudents)  # false  потому что единтичность не совподает


"""add"""
# students.append("sergei")  # добовляет в конец списка
# students.insert(2, "marat")  # добовляет в опр место в списке
# students.extend(["marat", "kamila"])  # добовляет несколько обк в конец списка


"""edit"""
# students.sort()  # сортировка
# students.reverse()  # реверсия списка
# students[1] = "hangaMarat" # изминение обк в опр месте


"""delete"""
# students.remove("marat")  # удалить по имени
# students.pop(-1)  # удаляет по индексу
# students.clear() # это rm -rf
# del students[:2]
# deleted students.pop(-1)  # вырезает по индексу хроня в себе тот обк

# print(students)
"""Индексы"""

# print(students[0])
# print(students[2])
# print(students[-1])
# print(students[-2])

# """срезы [start:stop:step]"""
# print(students[1:3:1])
# print(students[::2])


# print(type(sudents))

"""keyboard"""
while True:
    rus = 'й ц у к е н г ш щ з х ъ \ ф ы в а п р о л д ж э я ч с м и т ь б ю .'
    eng = "q w e r t y u i o p [ ] \ a s d f g h j k l ; ' z x c v b n m , . /"

    print("\nВыберите Команду\n1) с рус на англ\n2) c англ на рус \n0) выход")
    print("[-------------------------]")
    userInput = input("ввидите число команды: ")

    if userInput == "1":
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        rusInput = str(input("\nВвидите англ слово\nНа рус клаве:   "))

        result = ""
        for char in rusInput:
            if char in rus:
                index = rus.index(char)
                result += eng[index]
            else:
                result += char
        print(f'слово на англ {result}')
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    elif userInput == "2":
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        engInput = str(input("\nDвидите рус слово\nНа англ клаве:   "))
        result = ''
        for char in engInput:
            if char in eng:
                index = eng.index(char)
                result += rus[index]
            else:
                result += char
        print(f'слово на рус: {result}')
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    elif userInput == "0":
        break
