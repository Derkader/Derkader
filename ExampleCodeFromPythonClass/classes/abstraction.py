from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


@Shape.register
class Rectangle():
    def __init__(self, h, b):
        self.height = h
        self.base = b

    def area(self):
        return self.height*self.base


# driver
s = Rectangle(12, 12.4)
print(s.area())
