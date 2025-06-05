# Создание базового класса "Фигура" и его наследование для создания классов
# "Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
# такие как вычисление площади и периметра, а классы-наследники будут иметь
# специфичные методы и свойства.

import math


class Figure:

    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределён.")

    def perimeter(self):
        raise NotImplementedError("Метод perimeter() должен быть переопределён.")


class Square(Figure):
    """Класс для квадрата."""
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Rectangle(Figure):
    """Класс для прямоугольника."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Figure):
    """Класс для круга."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Пример использования
square = Square(5)
rectangle = Rectangle(4, 6)
circle = Circle(3)

print("Квадрат: площадь =", square.area(), ", периметр =", square.perimeter())
print("Прямоугольник: площадь =", rectangle.area(), ", периметр =", rectangle.perimeter())
print("Круг: площадь =", round(circle.area(), 2), ", длина окружности =", round(circle.perimeter(), 2))
