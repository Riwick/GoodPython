from math import e


d = dict.fromkeys([1, 2, 3])
print(d)

d = dict.fromkeys([1, 2, 3], "number")
print(d)

d.clear()
print(d)

d = {True: 1, False: "Lie", "list": [1, 2, 3], 5: 5}
c = d.copy()
print(c, d)
del c[5]
print(c, d)

c = dict(d)
print(id(c) == id(d))

print(d.get("list"))
print(d["list"])

# d[3] - error
# d.get(3) - None

print(d.get("1231"))

print(d.get(3, False))

print(d.setdefault(5, 123))
print(d.setdefault(6, 123))
print(d)

del d[6]

print(d.setdefault(3))
print(d)

print(d.pop(3))

print(d.pop(123, False))

print(d.popitem(), d)

# dict is an ordered collection! from python 3.7

print(d.popitem())

d2 = {}
# print(d2.popitem()) - error

print(d.keys())

d = {True: 1, False: "Lie", "list": [1, 2, 3], 5: 5}
print(d.keys())

for x in d:
    print(x, end=", ")

print()

print(d.values())

for x in d.values():
    print(x, end=", ")

print()

print(d.items())

for x in d.items():
    print(x, end=", ")

print()

x, y = (1, 2)
print(x, y)

for key, value in d.items():
    print(key, value, end=", ")

print()

d = dict(one=1, two=2, three=3, four=4)

lst = [[2, "bad"], [3, "ok"], ["four", "good"], [5, "well"]]
d2 = dict(lst)

d.update(d2)
print(d)

d = dict(one=1, two=2, three=3, four=4)

print({**d, **d2}) # like d.update(d2)
print({**d2, **d}) # like d2.update(d)

print(d | d2) # print({**d, **d2}) from python 3.9

