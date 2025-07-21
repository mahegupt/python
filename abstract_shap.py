from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Ractangle(Shape):
    def __init__(self, width, hight):
        self.width = width
        self.hight = hight

    def area(self):
        return self.width * self.hight

    def perimeter(self):
        return 2 * (self.width + self.hight)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


if __name__ == "__main__":
    rectange = Ractangle(10, 20)
    circle = Circle(10)
    print(
        f"Area of ractange is {rectange.area()} parameter is {rectange.perimeter()}")
    print(
        f"Area of ractange is {circle.area()} parameter is {circle.perimeter()}")
