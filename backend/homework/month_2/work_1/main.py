import os
from time import sleep


# class SuperHero():
#     # вызов класса

#     people = "people"
#     # без полезная чтука

#     def __init__(self, name: str, nickName: str, superPower: str, healthPoints: int, catchPhrase: str) -> tuple[str, int]:
#         self.name = name
#         self.nickName = nickName
#         self.superPower = superPower
#         self.healthPoints = healthPoints
#         self.catchPhrase = catchPhrase
#     # параметры для нашего класса

#     def getName(self):
#         return self.name
#     # say name broh

#     def doubleHealth(self):
#         self.healthPoints *= 2
#     # на 2 умнж

#     def __str__(self):
#         # мажик str первращяет все в строку то что в классе
#         returns = "\n"+f'\n============================\nname: {self.name};\n{self.nickName}: [{
#             self.superPower}],\n---------------------------- \n*** -=- Health = {self.healthPoints} -=- ***\n============================'
#         sleep(2)
#         os.system('clear')
#         return returns

#     def __len__(self):
#         return len(self.catchPhrase)
#     # если вернуть класс в len() то len вернет длину коронной


# hero = SuperHero("Klark ken", "Supermen",
#                  "Lazer, Fly, MegaPower superSpead", 1000, "I am a Super !!!")
# # obj для hero

# hero2 = SuperHero("Brus Wahin", "Batman",
#                   'his power it\'s just Human', 100, "Im a batman btw !!!")
# # obj для hero2


# hero.getName()

# print(hero)
# print(hero2)
# print("\n")
# print(f'Коронная фраза {hero.getName()}: {len(hero)} - букв')
# print(f'Коронная фраза {hero2.getName()}: {len(hero2)} - букв')


# ------------Dop-work-----Coffimachine-------------------------

class Coffimachine():
    # def __init__(self, start, water, readyCoffi, info, ):
    def __init__(self, name, brend, water: int, ):
        self.water = water
        self.NoWater = 0
        self.name = name
        self.brend = brend

    def start(self) -> str:
        try:
            print("наливаем воду !!!")
            while self.NoWater <= self.water:
                print(f'налито: {self.NoWater} литров')
                self.NoWater += 1
                sleep(0.5)
            return '\nУспешно !!!'

        except KeyboardInterrupt:
            print("\nвы остановили процесс")
            return "\nпроцесс завершен"

    coffiTypes = ['capuchin', 'classck', 'express', 'cocao']
    option = {
        "yes":"с cахaром",
        "y":"с cахaром",
        "no":"без сахара",
        "n":"без сахара"
    }
    def rdyCoffi(self, type: str, sugar: str) -> str:
        if type in self.coffiTypes and sugar in self.option:
            return f'ваш Коффе: {type} и {self.option[sugar]}'
        return "не корекный ввод"



    def info(self) -> str:
        text1 = f'\n  Coffimachine\nназвание машины: {self.name}\nбренд машины: {
            self.brend}\nобщее количество воды в машине:'
        text2 = f'{self.NoWater}\nвы налили {self.water}'
        return f'{text1} {text2}'

    def __str__(self) -> str:
        return f'\n   CoffiMachine:\n Имя: {self.name}\n Бренд: {self.brend}\n Воды:{self.water}\n'


coffi = Coffimachine("a1545", "Viteg", 10)

noCandy = coffi.rdyCoffi("express", "no")
coffiInfo = coffi.info()
startCoffi = coffi.start()

print(coffiInfo)
sleep(0.3)
print(startCoffi)
sleep(0.3)
print(noCandy)


"""
Что я сделал?
Я написал на Python шаблон для героев и дополнительно разработал шаблон для кофемашинки.

Какие проблемы я испытал?
Проблемы были с кофемашинкой, а именно с реализацией её работы. Я не смог сделать так, чтобы в цикле использовался return, а не print. Я мог создать переменную и увеличивать её значение, а затем вернуть результат, но это выглядело не очень красиво. Только с этим я столкнулся, а в остальном всё было нормально.

Что я буду делать дальше?
Я планировал сделать некую меню, где при выборе опции 1 можно было бы редактировать название машинки и бренд, а при выборе опции 2 — добавлять общее количество воды. Также хотел сделать красивый вывод при нажатии на 0.
"""
