#!/usr/bin/env python
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_perimeter(x1, y1, x2, y2, x3, y3):
    side1 = distance(x1, y1, x2, y2)
    side2 = distance(x1, y1, x3, y3)
    side3 = distance(x2, y2, x3, y3)
    return side1 + side2 + side3

def calculate_area(x1, y1, x2, y2, x3, y3):
    side1 = distance(x1, y1, x2, y2)
    side2 = distance(x1, y1, x3, y3)
    side3 = distance(x2, y2, x3, y3)
    poluperimeter = (side1 + side2 + side3) / 2
    return math.sqrt(poluperimeter * (poluperimeter - side1) * (poluperimeter - side2) * (poluperimeter - side3))

x1, y1 = map(float, input("Введите координаты вершины A через пробел: ").split())
x2, y2 = map(float, input("Введите координаты вершины B через пробел: ").split())
x3, y3 = map(float, input("Введите координаты вершины C через пробел: ").split())

perimeter = calculate_perimeter(x1, y1, x2, y2, x3, y3)
area = calculate_area(x1, y1, x2, y2, x3, y3)

print("Периметр треугольника равен", perimeter)
print("Площадь треугольника равна", area)