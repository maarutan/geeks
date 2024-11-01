# OOP
# Class
obj = "a"
from pathPY import Name


marat = Name("marat", "arzymatov", 16)

marat.sayName()


def a(b):
    print(b)


class Car:
    name = "MERS"

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def sayname(self):
        print(self.name)

    def __str__(self):
        return f"{self.model} {self.year}"


mers = Car("bmw", 1999)
mers2 = Car("312", 2010)

if __name__ == "__main__":
    print(type(obj))
    print(len(mers))
    print(mers2)
    a(7)
# обьект\экземпляр
