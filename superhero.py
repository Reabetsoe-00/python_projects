class Superhero:
    def __init__(self, name, alias, power, origin):
        self.name = name              # Public attribute
        self._alias = alias           # Protected attribute (encapsulation)
        self.__origin = origin        # Private attribute (encapsulation)
        self.power = power

    def introduce(self):
        print(f"I am {self.name}. I am known as {self._alias}. My superpower is {self.power}.")

    def get_origin(self):
        return f"My origin is {self.__origin}."

    def use_power(self):
        print(f"{self._alias} uses their power: {self.power}!")


class SuperStrength(Superhero):
    def __init__(self, name, alias, power, origin, super_strength):
        super().__init__(name, alias, power, origin)
        self.super_strength = super_strength

    # Method overriding: polymorphism
    def use_power(self):
        print(f"{self._alias} breaks through buildings with ease with his {self.power}!")


class Speedster(Superhero):
    def __init__(self, name, alias, power, origin, run_speed):
        super().__init__(name, alias, power, origin)
        self.run_speed = run_speed

    def use_power(self):
        print(f"{self.name} runs at {self.run_speed} km/h with his {self.power}!")


# Create superhero instances
hero1 = SuperStrength("Bruce Banner", "The Hulk", "Super Strength", "Earth", 0)
hero2 = Speedster("Barry Allen", "The Flash", "Super Speed", "Central City", 7500)


hero1.introduce()
hero1.use_power()
print(hero1.get_origin())

print()

hero2.introduce()
hero2.use_power()
print(hero2.get_origin())
