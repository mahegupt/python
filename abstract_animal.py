"""
In Python, you can define an abstract class using the abc module. 
An abstract class cannot be instantiated directly, and it can have one or more abstract methods, 
which must be implemented (redefined) by any subclass.
"""

from abc import ABC, abstractmethod

# Abstract base class


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass  # This method must be overridden in any subclass

# Child class 1


class Dog(Animal):
    def speak(self):
        return "Woof!"

# Child class 2


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Trying it out
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
