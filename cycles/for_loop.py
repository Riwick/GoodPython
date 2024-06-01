"""
for <variable> in <iterable_object>: - heading
    <operator_1>
    <operator_2> - body
    <operator_n>
"""

d = [1, 2, 3, 4, 5]

for i in d:
    print(i)

for x in "python":
    print(x, end=", ")

print()

for x in d:
    print(x)
    x = 0

for i in [0, 1, 2, 3, 4]:
    d[i] = 0

print(d)

# range(start, stop, step)

for i in range(5):
    print(i)

a = list(range(5))
print(a)

b = list(range(2))
print(b)

c = list(range(-10, -5))
print(c)

d = list(range(-10, -5, 2))
print(d)

e = list(range(-10, -5, -2))
print(e)

d = [1, 2, 3, 4, 5]

for i in range(len(d)):
    d[i] = 1

print(d)

sum = 0

for i in range(2, 1001):
    sum += 1/i

print(f"{sum:.3f}")
