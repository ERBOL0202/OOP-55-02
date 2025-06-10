#НАСЛЕДОВАНИЕ
#ПОЛИМОРФИЗ

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        print(f"{self.name} action!!!")

class WarriorHero(Hero):
    def __init__(self, name, lvl, hp, st):
        super().__init__(name, lvl, hp)
        self.st = st
    def action(self):
        print(f"WarriorHero!!!")
hero_1 = WarriorHero("Hero 1", 11, 100, 1000)
hero_1.action()