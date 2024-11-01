"""Урок 1. Тема №1. OOП 1: Основы ООП,
Создание первых классов, Атрибуты и Методы классов,
Принцип ООП - Наследование."""

"home work:"

"""
1. Создать класс Person с атрибутами full_name, age, is_married

2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке

3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.

4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам

5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience. 

6. Добавить в класс Teacher атрибут уровня класса base_salary.

7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к базовой зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.

8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату

9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.

10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.
"""


# class WahtYourName:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def youHaveGf(self, gf):
#         self.gf = gf
#         return f"your girl friend is {self.gf}"

#     def __str__(self):
#         return f"name: {self.name}, surname: {self.surname}, age: {self.age}"


# vasya = WahtYourName("Vasya", "Pupkin", 25)
# vasyaGF = vasya.youHaveGf("Masha")
# print(vasyaGF)
# print(vasya)


# class yourProfession(WahtYourName):
#     def __init__(self, name, surname, age, prof, year):
#         super().__init__(name, surname, age)
#         self.prof = prof
#         self.year = year

#     def __str__(self):
#         return f"{super().__str__()}\nyour profession is {self.prof} how many work {self.year} years"

#     def nameCompany(self, nc):
#         self.nc = nc
#         return f"your company is {self.nc}"


# class You(WahtYourName, yourProfession):

#     def __init__(self, name, surname, age, prof, year):
#         super().__init__(self, name, surname, age)
#         yourProfession.__init__(self, prof, year)

# def __str__(self):
#     return f"{super().__str__(self)}\n{yourProfession.__str__(self)}"


# marat = yourProfession("marat", "arzymatov", 25, "programmer", 3)
# print()
# print(marat)
