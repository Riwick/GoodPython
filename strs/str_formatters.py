import datetime
from random import randint


print("2 * 2 = %s" % (2 * 2))

print("2 * 2 = %s" % 2 * 2)

print("5 / 3 = ", 5/3)
print("5 / 3 = %.3f" % (5/3))
# print("5 / 3 = %.3f" % 4 / 7) - error

print('Округляем 0.000005:', "%.5f" % (0.000005))

[print("%c" % randint(0, 9999), end=" ") for _ in range(10)]
print()
[print("%d" % randint(0, 9999), end=" ") for _ in range(10)]
print()

print("%(15)s, %(second).5f" % {"15": "XX", "second": 0.5 ** 1.12})

"""
d - int
s - str
f - float
c - symbol
"""

print("Первый аргумент: {}, второй аргумент: {}".format(1, 2,))
print("Первый аргумент: {0}, третий аргумент: {2}".format(1, 2, 3,))

print("Первый аргумент: {0:+06d}, "
"второй аргумент: {second:>10b}".format(-1, 3, second=2,))

"""
d - 1 ... 10
f - float
c - Unicode symbol by number
b - 0 ... 1 (binary)
o - 0 ... 8 (oct)
x - 0 ... f (hex.lower())
X - 0 ... F (hex.upper())
"""

print("Здравствуйте, {}. "
"Глубина Вашего внутреннего мира {км:d} км."
.format("Изольда", км=0))

print("Здравствуйте, {}. "
"Глубина Вашего внутреннего мира {км:f} км."
.format("Изольда", км=0.3))

print("Здравствуйте, {}.\n"
"Глубина Вашего внутреннего мира\n"
"в двоичной/восьмиричной/шестнадцатеричной"
" системах:\n{км:b}/{км:o}/{км:x} км."
.format("Изольда", км=999))

# print("Здравствуйте, {}. "
# "Глубина Вашего внутреннего мира {км:d} км."
# .format("Изольда", км=0.3)) - error

print("{:20d}".format(3))
print("{:2d}".format(333))
print("{:7.4f}".format(3.14))
print("{:03d}".format(7))
print("{:08.3f}".format(12.2346))

"""
< - left border
^ - center
> - right border
= - move signs ( + or - ) to left
"""

print("{:7d}".format(7))
print("{:^7.1f}".format(3.14))
print("{:=07.1f}".format(-3.14))


print("{:10}-Питончик".format("Python"))
print("{:>10}-Питончик".format("Python"))
print("{:^10}-Питончик".format("Python"))
print("{:_^10}-Питончик".format("Python"))
print("{:_^20}-Питон".format("Python"))

print("{:.2}-Питончик".format("Python"))
print("{:^10.3}".format("Python"))
print("{:10.2}-Питончик".format("Python"))
print("{:_^6.2}-Питончик".format("Python"))

string = "{:{заполнитель}{выравнивание}{ширина}}"
print(string.format('Питон', заполнитель='_', выравнивание='^', ширина=9))
string = '{:{}{}{}}'
print(string.format('Питон', '_', '^', 9))

current_datetime = datetime.datetime.now()
print("Сейчас: {:%d.%m.%Y %H:%M}".format(current_datetime))
my_complex = 3+14j
print("Реальная часть: {0.real} мнимая часть: {0.imag}".format(my_complex))

print(format(1, 'f'))
print(format(1000, '#>+10,.2f'))
print(format(999.99, ">5,.2f"))
print(format(1000.5368, '~>+15,.2f'))
print(format('format', '.2'))

age = 18
name = "Riwi"

# Python 3.6

print(f"My name is {name}, I\"m {age} years old")
print(F"My name is {name.upper()}, I\"m {age * 2} years old")
print(f"My name is {len(name)}, I\"m {age * 2} years old")

print(f'2 + 2 = {2 + 2:010d}')
print(f'2 + 2 = {2 + 2:^010d}')
print(f'2 + 2 = {"четыре":.3}')
print(f"2 + 2 = {2 + 2:_>10d}")


# f-strings are the fastest than another ways to format strings in python
