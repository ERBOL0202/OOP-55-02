class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def introduse(self):
        print (f"Привет меня зовут {self.name}, мне age {self.age}, мой city {self.city}")
    def is_adult(self):
        return self.age >= 18
person1 = Person("Джинву", 24)
person2 = Person("ДжинА", 16)
print = (f"{person1.name} - {person1.is_adult()}")
print = (f"{person2.name} - {person2.is_adult()}")


