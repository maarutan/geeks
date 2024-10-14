import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../work_1"))

from hero import SuperHero  # type: ignore


class newHero(SuperHero):
    people = "Hero"

    def __init__(
        self,
        name: str,
        nickName: str,
        superPower: set,
        healthPoints: int,
        catchPhrase: str,
        damage: int = 0,
    ) -> None:
        super().__init__(name, nickName, superPower, healthPoints, catchPhrase)
        self.damage = damage
        self.fly = False

    def doubleHealth(self):
        self.healthPoints **= 2
        self.fly = True
        return self.healthPoints

    def TrueInThe(self):
        return f"TrueInThe: {self.catchPhrase}"

    def __str__(self):
        parentStr = super().__str__()
        return f"{parentStr}\nfly?: {"yes" if self.fly else "no"}\n----------------------------\n============================"


class villain(newHero):
    people = "monster"

    def __init__(
        self,
        name: str,
        nickName: str,
        superPower: set,
        healthPoints: int,
        catchPhrase: str,
        damage: int = 0,
    ) -> None:
        super().__init__(name, nickName, superPower, healthPoints, catchPhrase, damage)

    def gen_x(self) -> None:
        pass

    def crit(self):
        self.damage **= 2
        return self.damage


monster1 = villain(
    "marat",
    "maaru",
    "programming",
    100,
    "IUseArchBtw",
)
print(monster1.crit())
hero1 = newHero("marat", "maaru", "programming", 100, "IUseArchBtw")
print(hero1.doubleHealth())
print(hero1)
