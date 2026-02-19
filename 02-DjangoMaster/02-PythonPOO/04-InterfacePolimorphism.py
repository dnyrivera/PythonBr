from abc import ABC, abstractmethod
import math


class Shape(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


def print_area(shape: Shape):
    print(f"The are of the {shape.name} is: {shape.area():.2f}")


circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 7)

print_area(circle)
print_area(rectangle)
print_area(triangle)
