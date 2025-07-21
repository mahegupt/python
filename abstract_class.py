import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def parimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def name(self):
        return "Circle"

    def area(self):
        return math.pi * self.radius * self.radius

    def parimeter(self):
        return 2 * math.pi * self.radius


class Ractangle(Shape):
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def name(self):
        return "Ractangle"

    def area(self):
        return self.hight * self.width

    def parimeter(self):
        return 2 * (self.hight + self.width)


shapes = [Circle(10), Ractangle(10, 20)]

for shape in shapes:
    print(f"{shape.name()}: Area = {shape.area():.2f}, Perimeter = {shape.parimeter():.2f}")
