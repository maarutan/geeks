"""Инкапцуляция"""

# Уровни доступа
# 1 - это публичный
# 2 - защищенный protected


class Bank:
    def __init__(self, name: str, age: int, ballance: float) -> None:
        self.name = name
        self._validateAge(age)
        self.age = age
        self._ballance = ballance  # protected

    def _validateAge(self) -> None:
        if self._age < 18:
            raise ValueError("your age must 18+")

    # protected 2 метод инкапцуляции а тоесть защищенный
    # potected - придуприжедение о не изменности в не класса

    def __str__(self) -> str:
        return (
            f"name: {self.name}\n" f"age: {self._age}\n" f"ballance: {self._ballance}\n"
        )


""" Публичный Уровень Доступа  1 - уровень инкасуляции """
user1 = Bank("beka", 18, 1000)
user1._age = 18
user1.name = "bekbolot"
user1.ballance = 1000000
print(user1)


# user2 = Bank("marat", 16, 1000)
# print(user2)
