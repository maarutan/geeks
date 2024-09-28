"""Словари, Множества"""
# {key: value}
from time import sleep
students = {
    "name": "marat",  # key
    "age": 16  # value
}


"""Доступ к Значениям Словаря """
# print(students)
# print(students["name"])
# print(students.get("nam", 'нету такого ключа'))


"""add"""
students["surname"] = "arzymatov"  # добавить 1 обЪект

students.update({  # добавить несколько обЪектов
    "height": 1.85,
    "weight": 71.80
})

"""edit"""
students["age"] = 17  # редактировать
students["name"] = "HangaMarat"  # редактировать

"""delete"""
students.pop("weight")  # вырезать
del students["height"]  # удалять
students.clear  # очистить


# for i in students:
# sleep(1)
# print(f'{i}: {students[i]}')


# print(students.keys())
# print(students.values())
# print(students.items())


# for key, item in students.items():
#     print(f"{key} - {item}")


numbers1 = [1, 2, 3, 4, 2, 1, 3, 5, ]
numbers2 = (1, 2, 3, 4, 2, 1, 3, 5, )
numbers3 = {1, 2, 3, 4, 2, 1, 3, 5, }

print(numbers1)
print(numbers2)
print(numbers3)


"""
типы данных 


Словарь - set
Кортеж - tuple
Cписок - list


число - int
стока - str
боол - bool

"""


time = input("enter time: ").lower()
searWord = set(time).issubset("утро morning день day вечер evening")
rusWord = set(time).issubset("утро день вечер")
engWord = set(time).issubset("morning day evening")

if time in "утро" or time in ("morning") or searWord:
    if time in "утро" or rusWord:
        print(f"Доброе {time}".title)
    elif time in "morning" or engWord:
        print(f'have a good {time}')
elif time in "день" or time in ("day") or searWord:
    if time in "день" or rusWord:
        print(f"Добрый {time}".title)
    elif time in "day" or engWord:
        print(f'have a good {time}')
elif time in "вечер" or time in ("eveningh") or searWord:
    if time in "вечер" or rusWord:
        print(f"Доброе {time}".title)
    elif time in "morning" or engWord:
        print(f'have a good {time}')


"""Cписок & Лист"""

# students = ['endar', 'nurdan', 'dariya']
# students[0] = "marat"

# print(students[-1])
# print(students[:2])
# print(students)
