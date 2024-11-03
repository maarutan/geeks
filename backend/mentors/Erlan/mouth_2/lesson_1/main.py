"""Урок 1. Тема №1. OOП 1: Основы ООП,
Создание первых классов, Атрибуты и Методы классов,
Принцип ООП - Наследование."""

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


"""
 _                                   _   
| |_  ___ _ __  ___  __ __ _____ _ _| |__
| ' \/ _ \ '  \/ -_) \ V  V / _ \ '_| / /
|_||_\___/_|_|_\___|  \_/\_/\___/_| |_\_\
                                         
"""
import os


class Person:
    def __init__(self, fullName, age, isMarried=False) -> None:
        self.fullName = fullName
        self.age = age
        self.isMarried = isMarried
        self.yesNO = {"n": False, "no": False, "y": True, "yes": True}

    def introduceMyself(self):
        if self.yesNO.get(str(self.isMarried).lower(), False):
            return f"Hello,\nmy name is\n{'-' * 20}\n{self.fullName}\nI'm {self.age} years old\nI'm married"
        else:
            return f"Hello,\nmy name is\n{'-' * 20}\n{self.fullName}\nI'm {self.age} years old\nI'm single"

    def __str__(self) -> str:
        return self.introduceMyself()


class Students(Person):
    def __init__(
        self,
        fullName,
        age,
        marks=None,
        isMarried=False,
    ) -> None:
        super().__init__(fullName, age, isMarried)
        self.marks = marks if marks else {}

    def showMarks(self):
        return "\n".join(
            f"subject: {key}, mark: {value}" for key, value in self.marks.items()
        )

    def infoStudents(self):
        return f"{super().__str__()}"  # type: ignore

    def NormalBall(self):
        os.system("clear")
        return f"{self.fullName} normal ball is {sum(self.marks.values()) / len(self.marks)}"

    def __str__(self) -> str:
        os.system("clear")
        return super().__str__() + f"\n{"-"*30}" + f"\n{self.showMarks()}"


class Teachers(Person):
    def __init__(
        self,
        fullName,
        age,
        experience,
        baseSalary,
        isMarried=False,
    ):
        super().__init__(fullName, age, isMarried)
        self.experience = experience
        self.baseSalary = baseSalary
        self.bonuses = 0

    def Bonus(self):
        bonusYears = max(0, self.experience - 3)
        bonus = self.baseSalary * 0.05 * bonusYears
        self.bonuses += self.baseSalary + bonus
        return self.bonuses

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"\nexperience: {self.experience} years\nbase salary: {self.baseSalary}\nbonus: {self.bonuses}"
        )


gojoSatoru = Teachers("Gojo Satoru", 28, 5, 1000)
gojoSatoru.Bonus()
gojoSatoru.Bonus()
gojoSatoru.Bonus()
gojoSatoru.Bonus()
gojoSatoru.Bonus()
gojoSatoru.Bonus()
gojoSatoru.Bonus()
gojoSatoru.Bonus()

print(gojoSatoru)
