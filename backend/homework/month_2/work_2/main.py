import sys
import os
from time import sleep

sys.path.append((os.path.join(os.path.dirname(__file__), "../work_1")))
from hero import SuperHero  # type: ignore


class SuperHero:  # noqa: F811
    people = "people"

    def __init__(
        self,
        name: str,
        nickName: str,
        superPower: str,
        healthPoints: int,
        catchPhrase: str,
        damage: int,
    ):
        self.name = name
        self.nickName = nickName
        self.superPower = superPower
        self.healthPoints = healthPoints
        self.catchPhrase = catchPhrase
        self.damage = damage
        self.fly = False

    def getName(self):
        return self.name

    def doubleHealth(self):
        self.healthPoints **= 2
        self.fly = True

    def truePhrase(self):
        return f"True in the {self.catchPhrase}"

    def __str__(self):
        sleep(2)
        os.system("clear")
        return (
            f"\n============================\n"
            f"Имя: {self.name};\n"
            f"{self.nickName}: [{self.superPower}],\n"
            f"---------------------------- \n"
            f"*** -=- Здоровье = {self.healthPoints} -=- ***\n"
            f"Урон = {self.damage}, Флай = {self.fly}\n"
            f"============================"
        )

    def __len__(self):
        return len(self.catchPhrase)


class AirHero(SuperHero):
    def __init__(self, name, nickName, superPower, healthPoints, catchPhrase, damage):
        super().__init__(name, nickName, superPower, healthPoints, catchPhrase, damage)


class EarthHero(SuperHero):
    def __init__(self, name, nickName, superPower, healthPoints, catchPhrase, damage):
        super().__init__(name, nickName, superPower, healthPoints, catchPhrase, damage)


class SpaceHero(SuperHero):
    def __init__(self, name, nickName, superPower, healthPoints, catchPhrase, damage):
        super().__init__(name, nickName, superPower, healthPoints, catchPhrase, damage)


class Villain(SuperHero):
    people = "monster"

    def gen_x(self):
        pass

    def crit(self, multiplier: int):
        self.damage **= multiplier


airHero = AirHero(
    "Skyler", "Windman", "Fly, Storm Control", 800, "I rule the skies!", 50
)
earthHero = EarthHero(
    "Terra", "Earthquake", "Earth Manipulation", 900, "Feel the ground shake!", 70
)
spaceHero = SpaceHero(
    "Galaxor", "Starshine", "Gravity Control", 1000, "I am the cosmos!", 100
)

print(airHero)
airHero.doubleHealth()
print(airHero.truePhrase())

print(earthHero)
earthHero.doubleHealth()
print(earthHero.truePhrase())

print(spaceHero)
spaceHero.doubleHealth()
print(spaceHero.truePhrase())

villain = Villain("Evilman", "Villainous", "Chaos Control", 500, "I am your doom!", 80)
villain.crit(2)
print(f"Damage злодея {villain.getName()}: {villain.damage}")

airHero.healthPoints -= villain.damage
print(f"Здоровье {airHero.getName()} после атаки злодея: {airHero.healthPoints}")
