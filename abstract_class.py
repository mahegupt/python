from abc import ABC, abstractmethod


class shap(ABC):
    @abstractmethod
    def area():
        pass


class circle(shap):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


c = circle(2)
print("Area of circle is ", c.area())
