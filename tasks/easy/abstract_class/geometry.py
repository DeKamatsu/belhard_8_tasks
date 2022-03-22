"""
Описать абстрактный класс Shape - фигура, у которого:

- абстрактный метод get_perimeter (не принимает аргументов) для расчета периметра
- абстрактный метод get_square (не принимает аргументов) для расчета площади

Во всех дочерних классах методы get_perimeter и get_square должны возвращать
результат вычислений.

Описать класс Circle для круга (дочерний класс для Shape), у которого:

- атрибут r - радиус, тип float
- магический метод __init__, который принимает r
- перегрузить метод get_perimeter (формула длины окружности: 2 * pi * r)
- перегрузить метод get_square (формула площади: pi * r ** 2)

Описать класс Rectangle для прямоугольника (дочерний класс для Shape), у которого:

- атрибут a - первая сторона, тип float
- атрибут b - вторая сторона, тип float
- магический метод __init__, который принимает a и b
- перегрузить метод get_perimeter (формула периметра: 2 * (a + b))
- перегрузить метод get_square (формула площади: a * b)

Описать класс Square для квадрата (дочерний класс для Rectangle), у которого:

- магический метод __init__, который принимает a, вызывает super
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    абстрактный класс Shape - фигура, у которого:

    - абстрактный метод get_perimeter (не принимает аргументов) для расчета периметра
    - абстрактный метод get_square (не принимает аргументов) для расчета площади
    """
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):
    """
    Описать класс Circle для круга (дочерний класс для Shape), у которого:

    - атрибут r - радиус, тип float
    - магический метод __init__, который принимает r
    - перегрузить метод get_perimeter (формула длины окружности: 2 * pi * r)
    - перегрузить метод get_square (формула площади: pi * r ** 2)
    """
    r: float

    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        return 2 * pi * self.r

    def get_square(self):
        return pi * self.r ** 2


class Rectangle(Shape):
    """
    Описать класс Rectangle для прямоугольника (дочерний класс для Shape), у которого:

    - атрибут a - первая сторона, тип float
    - атрибут b - вторая сторона, тип float
    - магический метод __init__, который принимает a и b
    - перегрузить метод get_perimeter (формула периметра: 2 * (a + b))
    - перегрузить метод get_square (формула площади: a * b)
    """
    a: float
    b: float

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_square(self):
        return self.a * self.b


class Square(Rectangle):
    """
    Описать класс Square для квадрата (дочерний класс для Rectangle), у которого:

    - магический метод __init__, который принимает a, вызывает super
    """

    def __init__(self, a):
        super().__init__(a, b=a)
        self.a = a
        self.b = a


# a = Circle(5)
# print(a.get_perimeter(), a.get_square())
#
# a = Rectangle(5, 7)
# print(a.get_perimeter(), a.get_square())
#
# a = Square(10)
# print(a.get_perimeter(), a.get_square())
