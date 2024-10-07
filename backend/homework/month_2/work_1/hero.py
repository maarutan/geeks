import os
from time import sleep


class SuperHero():
    # вызов класса

    people = "people"
    # без полезная чтука



    def __init__(self, name: str, nickName: str, superPower: str, healthPoints: int, catchPhrase: str) -> tuple[str, int]:
        self.name = name
        self.nickName = nickName
        self.superPower = superPower
        self.healthPoints = healthPoints
        self.catchPhrase = catchPhrase
    # параметры для нашего класса

    def getName(self):
        return self.name
    # say name broh

    def doubleHealth(self):
        self.healthPoints *= 2
    # на 2 умнж

    def __str__(self):
        # мажик str первращяет все в строку то что в классе
        returns = "\n"+f'\n============================\nname: {self.name};\n{self.nickName}: [{
            self.superPower}],\n---------------------------- \n*** -=- Health = {self.healthPoints} -=- ***\n============================'
        sleep(2)
        os.system('clear')
        return returns

    def __len__(self):
        return len(self.catchPhrase)
    # если вернуть класс в len() то len вернет длину коронной


hero = SuperHero("Klark ken", "Supermen",
                 "Lazer, Fly, MegaPower superSpead", 1000, "I am a Super !!!")
# obj для hero

hero2 = SuperHero("Brus Wahin", "Batman",
                  'his power it\'s just Human', 100, "Im a batman btw !!!")
# obj для hero2
