"""
По введенным пользователем координатам двух точек вывести уравнение
прямой вида y = kx + b, проходящей через эти точки
"""
x1 = int(input('Введите координаты точки x1: '))
x2 = int(input('Введите координаты точки x2: '))
y1 = int(input('Введите координаты точки y1: '))
y2 = int(input('Введите координаты точки y2: '))

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

print(k * x1 + b)