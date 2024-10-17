"""Инкапцуляция"""

# Уровни доступа
# 1 - это публичный
# 2 - защищенный protected
# 3 - Приваптный \ Cкрытый


class Bank:
    def __init__(self, name: str, age: int, ballance: float) -> None:
        self.name = name
        self._age = age
        self._validateAge(age)
        self.__ballance = ballance  # protected

    # protected 2 метод инкапцуляции а тоесть защищенный
    # potected - придуприжедение о не изменности в не класса

    def _validateAge(self, age) -> None:
        if age < 18:
            raise ValueError("your age must 18+")

    def getAge(self):
        print(self._age)
        return self._age

    def NewAge(self, newAge):
        self._validateAge(newAge)
        self._age = newAge
        print(f"youre age chages in {self._age} year")

    def __str__(self) -> str:
        return (
            f"\nname: {self.name}\n"
            f"age: {self._age}\n"
            f"ballance: {self.__ballance}\n"
        )


""" Публичный Уровень Доступа  1 - уровень инкасуляции """

user1 = Bank("beka", 18, 1000)
user1.name = "bekbolot"
# print(user1)


user1.getAge()
# inp = int(input("enter your new Age: "))
user1.NewAge(19)


print(user1)
# user2 = Bank("marat", 16, 1000)
# print(user2)
