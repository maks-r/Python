"""
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
"""
x = int(input('Введите трехзначное число: '))
a = x // 100
b = (x // 10) % 10
c = x % 10
print(a + b + c)
print(a * b * c)