x, y = (1, 2)
print(x, y)

x, *y = (1, 2, 3, 4)
print(x, y)

*x, y = (1, 2, 3, 4)
print(x, y)

x, *y = [1, "a", True, 4]
print(x, y)

*x, y, z = "python"
print(x, y, z)

# *x = 1, 2, 3 - error

*x, y = 1, 2, 3  # packing
print(x, y)
print(*x, y)

x = "string"
print(*x, max(*x))

a = [1, 2, 3]
print((a,))
print((*a,))  # unpacking


d = -5, 5
# range(d) - error
# range(*d) == range(-5, 5)
print(range(*d))

a = [range(*d)]
print(a)

a = [*range(*d)]
print(a)

a = [*range(*d), *(True, False), *a]
print(a)

d = {0: "worst", 1: "terrible", 2: "bad", 3: "ok", 4: "good", 5: "well"}

print(*d)  # only d.keys()
print(*d.values())
print(*d.items())

print({**d})

d2 = {6: "awesome", 7: "wonderful"}

# ** can be used only for unpacking, except **kwargs in function parameters
print({**d, **d2})
