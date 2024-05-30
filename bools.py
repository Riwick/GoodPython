print(4 > 2)
print(4 > 7)

a = 5
b = 6.7
print(a <= b)
res = a >= b
print(res, type(res), end="\n\n")

print(5 == 7-2, end="\n\n")

x = 6
print(x % 2 == 1)
print(x % 2 != 1, end="\n\n")

y = 3.85
print(2 <= y <= 5)
print(y >= 2 and y <= 5)
print(y < -2 or y > 5)
y = -10
print(y < -2 or y > 5, end="\n\n")

print(not (x % 2 == 0 and x % 3 == 0), end="\n\n")

# or = 1
# and = 2
# not = 3

print(bool())
print(bool(1))
print(bool(0))
print(bool("a"))
print(bool(" "))
