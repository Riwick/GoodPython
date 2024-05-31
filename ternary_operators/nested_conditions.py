x = int(input())

if x % 2 == 0:
    if 0 <= x <= 9:
        print("x is figure")
    else:
        print("x is number")
else:
    print("x is odd number")

item = int(input("item: "))

if item == 1:
    print("1 is the worst")
elif item == 2:
    print("2 is bad")
elif item == 3:
    print("3 is ok")
elif item == 4:
    print("4 is good")

"""
if condition:
    code
elif condition:
    code
else:
    code
"""

x = int(input())

if x < 0:
    print("Wrong number")
else:
    if 0 <= x <= 10:
        print("x is figure")
    elif 10 <= x <= 99:
        print("x is a two-digit number")
    elif 100 <= x <= 999:
        print("x is a three-digit number")

