from typing import Literal


print((1, 2, 3))

a = 1, 2
print(type(a), a)

a = (1, 2, 3)
print(a)

# a = 1, 2, 3 == a = (1, 2, 3)

b = (1)
print(type(b), b)

b = (1,)
print(type(b), b)

b = 2,
print(type(b), b)

x, y = (1, 2)
print(x, y)

x, y, z = (1, 2, 3)
print(x, y, z)

x, y = ["hello", "python"]
print(x, y)

a, b = "ra"
print(a, b)

a = 1, 2, 3
print(len(a))

print(a[0])

print(a[1:2])
print(a[0:2])

print(a[:]) # no copy
b = a[:]
print(id(a) == id(b))

# a[1] = 100 - error

d= {}
d[a] = "tuple"
print(d)

c = tuple([1, 2, 3])
print(c)

lst = [1, 2, 3]
a = (1, 2, 3)
print(lst.__sizeof__(), a.__sizeof__())

a = ()
print(type(a))

b = tuple()
print(type(b))

a += (1,)
print(a)

a = (2, 3) + a
print(a)

a += (("a", "hello"),)
print(a)

b = (0,) * 10
print(b)

b = ("hello", "world") * 5
print(b)

# del b[1] - error

a = tuple([1, 2, 3])
print(a)

a = tuple("hello")
print(a)

t = 1, 2, 3
print(list(t))

a = (True, [1, 2, 3], True, "hello", 5, {"house": "123"}, True)

a[1].append(5)
print(a)

# we can't change a tuple but we can change mutable objects in tuple, like list

print(a.count(True))
print(a.count(2))

print(a.index(True), a.index(True, 1), a.index(True, 3))
# print(a.index("123")) - error

print(3 in a, 1 in a, [1, 2, 3] in a)