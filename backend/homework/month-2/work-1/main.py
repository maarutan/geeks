class SuperHero:
    people = 'people'

    def __init__(self, name, nickName, superPower, healthPoints, catchPhrase):
        self.name = name
        self.nickName = nickName
        self.superPower = superPower
        self.healthPoints = healthPoints
        self.catchPhrase = catchPhrase

    def getName(self):
        return self.name

    def doubleHealth(self):
        self.healthPoints *= 2

    def __str__(self):
        return f"{self.nickName}: Superpower = {self.superPower}, Health = {self.healthPoints}"

    def __len__(self):
        return len(self.catchPhrase)


hero = SuperHero("Clark Kent", "Superman", "Flight",
                 100, "I am here to save the day!")

print(f"All heroes are {SuperHero.people}")
print(hero.getName())
print(hero.healthPoints)
hero.doubleHealth()
print(hero.healthPoints)
print(hero)
print(len(hero))
