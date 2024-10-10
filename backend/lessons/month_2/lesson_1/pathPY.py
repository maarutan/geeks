# OOP
# Class
obj = 'a'


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


class Name():
    def __init__(self,name,surame,age):
        self.name = name
        self.surname = surame
        self.age = age
    def sayName(self):
        print(self.name) 
        




if __name__ == '__main__':
    print(len(mers))
    print(mers2)
    print(type(obj))
# обьект\экземпляр
