class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def action(self):
        print(f"{self.hp} action")
    def attack(self):
        print(f"how hp left after attack{self.hp}")
class Archer(Hero):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(self, name, hp)
        self.arrows = arrows
        self.precision = precision
    def attack(self):
        self.arrows -= 1
        hit_chance = random.random()
        if hit_chance <= self.precision:
            print("Атака успешна")
        else:
            print("Атака не удалась")
    def rest(self):
        self.arrows += 5
        print("Стрелы пополнены")
    def status(self):
        base.status = super().status()
        return f"{base_status}: {self.arrows}: {self.precision}:"
