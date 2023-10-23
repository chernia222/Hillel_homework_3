
from abc import ABC, abstractmethod
import math


class Figure(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Round(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

def main():
    triangle = Triangle(3, 4, 5)
    circle = Round(7)

    figures = [triangle, circle]

    for figure in figures:
        print(f"Perimeter: {figure.perimeter()}")
        print(f"Area: {figure.area()}")
        print()

if __name__ == "__main__":
    main()