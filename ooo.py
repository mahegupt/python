class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I made a sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Chicken(Animal):
    def speak(self):
        return f"{self.name} says CoocrooKu!"


animals = [Dog("Bhodu"), Cat("Dirt"), Chicken("Chicks")]

for a in animals:
    print(a.speak())
