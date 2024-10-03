# ПРИНЦИПЫ ООП:НАСЛЕДОВАНИЕ,ПОЛИМОРФИЗМ,инкапсуляция абстракция
# множественное наследование
# gitignore / git rm --cached (-r)
# СУПЕР класс\РОДИТЕЛЬСКИЙ класс

from ..lesson_1.main import a  

print(a)
# print(mers2)


class Zavod:
    name = "Завод имени Артура"

    def __init__(self, id):
        self.id = id


# дочерний класс
class Bmw(Car, Zavod):
    # global name
    def __init__(self, model, year, id):
        super().__init__(model, year)
        Car.__init__(self, model, year)
        Zavod.__init__(self, id)

    def marks(self):
        print("официальный представитель BMW")


bmw = Bmw("x5", 2022, 1)
# bmw.marks()
print(Bmw.mro())
# MRO-порядок выполнения методов
bmw.sayname()
