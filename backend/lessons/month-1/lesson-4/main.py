### Списки, корежи, Индексы и срезы. Встроенные функции к наборам элементов.an
### Списковые вкючение List comprehesion.
# int, float, str ,bool
# print(bool(0))
# print(list('`geeks`'))


# number = [23, 45, 67, 89, 90, 11]

# print(len(number)) # return количество объектков
# print(min(number)) # return
# print(max(number)) # return максимальное число
# print(sum(number)) # return мимнимальное число
# print(any(number)) # return если есть в листе хотябы 1 true и return true
# print(all(number)) # return если есть в листе хотябы 1 false и return false

# students = ["bilal", "dair", "aidana", "ulan"]


# students = tuple(students)
# print(tuple(geeks))


# newStudents = students.copy()
# print(id(students))
# print(id(newStudents))
# print(students)
# print(newStudents)

"""tuple Kortege"""

# number = 34, 67, 46, 59, 87, 92,
# print(number)
# print(type(number))

"""add"""
# students.append("sergei")  # добавляет один объект в конец списка
# students.insert(2, "ali")  #  добавляет один объект в опр место
# students.extend(
#     ["marat", "kamila"]
# )  # добавляет один объект не один обк в конеуц списка

"""edit"""
# students.sort()
# students.reverse()
# students[0] = 'adel'

"""delete"""
# deleted = students.remove('dair')
# students.pop(-1)
# del students[:2]
# students.clear()


"""Индексы"""
# print(students[0])
# print(students[2])
# print(students[-1])
# print(students[-2])

"""Срезы [start:stop:step]"""
# print(students[1:3:1])
# print(students[:2])
# print(students[::2])


# print(type(students))
