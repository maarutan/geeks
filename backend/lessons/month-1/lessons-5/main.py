"""Словари множества"""

students = {"name": "Azamat", "age": "18"}


"""add"""
students["students"] = "dairbekov"
students.update({"whight": 67.4, "hight": 1.77, "name": "tilek"})

"""edit"""
students["age"] = 22

"""delete"""
del students["hight"]
students.clear()

numbers1 = [1, 2, 3, 4, 2, 1, 3, 5]
numbers2 = (1, 2, 3, 4, 2, 1, 3, 5)
numbers3 = {1, 2, 3, 4, 2, 1, 3, 5}

print(numbers1)
print(numbers2)
print(numbers3)

"""доступ к значениям словаря"""
# print(students["name"])
# print(students.get("name"))
