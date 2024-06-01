N = 6
a = [0] * N

for i in range(N):
    a[i] = i ** 2

print(a)


a = [i ** 2 for i in range(N)]
print(a)

"""
[<value_formation> for <variable> in <iterable_object> if <condition>]

[<value_formation>
for <variable> in <iterable_object>
if <condition>]
"""

a = [1 for i in range(6)]
print(a)

N = 7
a = [1 for i in range(N)]
print(a)

a = [x % 4 for x in range(1, 6)]
print(a)

a = [x for x in range(N) if x % 2 == 0]
print(a)
a = [x % 2 == 0 for x in range(N)]
print(a)

# d_inp = input("Numbers: ")

# a = [int(x) for x in d_inp.split()]
# print(a)
# a = list(map(int, input("Numbers: ").split()))
# print(a)

a = [d for d in "python"]
print(a)

a = [ord(x) for x in "python"]

t = ["I", "like", "to", "programming", "on", "python"]
a = [d for d in t]
print(a)

a = [len(d) for d in t]
print(a)

a = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]
print(a)

cities = ["Moscow", "Paris", "New-York", "Berlin"]

a = [city for city in cities if len(city) < 7]
print(a, len("New-York"))

d = [4, 3, -5, 0, 2, 11, 122, -8, 9]

a = [("even" if number % 2 == 0 else "odd") for number in d]
print(a)

a = ["even" if number % 2 == 0 else "odd"
     for number in d
     if number > 0]
print(a)

t = [1, 2, 3, 4, 5]
a = ["good" if x % 2 == 0 else "bad" for x in t]
print(a)