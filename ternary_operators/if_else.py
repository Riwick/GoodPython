
x = 4
if x < 0:
    x = abs(x)

    print(x)

a = float(input("a: "))
b = float(input("b: "))

if a < b:
    a, b = b, a

print(a, b)

x = int(input("x: "))

if -4 <= x <= 10:
    print("X more that -4 and less than 10")

x = True
if x:
    print("Now we have x!")

marks = input().split()
print(marks)

if "2" in marks:
    print("You are stupid")
else:
    print("You are not stupid")

x = int(input("x: "))
if x < 0:
    print("x less than zero")
else:
    print("x more than zero")
