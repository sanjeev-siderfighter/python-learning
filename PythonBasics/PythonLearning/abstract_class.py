from abc import ABC, abstractmethod


class Shape():
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth


rect = Rectangle(2, 5)
print(rect.get_area())

shape = Shape()
shape.get_area()