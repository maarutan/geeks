# OOP
# Class
obj = 'a'

print(type(obj))


def a(b):
    print(b)


p = a(7)


class Car:
    name = 'MERS'

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def sayname(self):
        print(self.name)

    def __str__(self):
        return f'{self.model} {self.year}'


mers = Car('bmw', 1999)
mers2 = Car('312', 2010)

if __name__ == '__main__':
    print(len(mers))
    print(mers2)
# обьект\экземпляр
