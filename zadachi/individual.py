#!/usr/bin/env python
x1, y1 = map(float, input("Введите координаты вершины A через пробел ").split())
x2, y2 = map(float, input("Введите координаты вершины B через пробел ").split())
x3, y3 = map(float, input("Введите координаты вершины C через пробел ").split())
a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
b = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
perimetr = a + b + c
poluperimetr = perimetr/2
s = (poluperimetr) * ((poluperimetr - a) * (poluperimetr - b) * (poluperimetr - c))**0.5

print("Периметр треугольника:", perimetr)
print("Площадь треугольника:", s)