
a = [1, -45, 3, 2, 100, -4]
a.sort()
print(a)

b = ("123", "234", "456")
# b.sort() - error because tuple is immutable

print(sorted(b))  # sorted can sort any iterable object
print(sorted("python"))  # sorted by ascii codes


try:
    a = [1, -45, 3, 2, 100, -4, "abc"]
    a.sort()
    print(a)
except TypeError:
    print("We can\'t sort a list with str and int")


try:
    a = [1, -45, 3, 2, 100, -4, "abc"]
    print(sorted(a))
except TypeError:
    print("We can\'t sort a list with str and int")

a = [1, 0, -5, 10, 20]
b = sorted([1, 0, -5, 10, 20])  # this is not the same list
print(a is b)

print(sorted(a, reverse=True))
print(sorted(("123", "234", "456"), reverse=True))


d = {"river": 1, "house": 2, "tree": 3, "road": 4}
print(sorted(d))
print(sorted(d.values()))
print(sorted(d.items()))

a = dict(sorted(d.items()))
print(a)


# key param

a = [4, 3, -10, 1, 7, 12]


def is_odd(x):
    return x % 2


print(sorted(a, key=is_odd))
print(sorted(a, key=lambda x: x % 2))

a.sort(key=lambda x: x % 2)
print(a)


def key_sort(x):
    return x if x % 2 == 0 else 100 + x


print(sorted(a, key=key_sort))


lst = ["abc", "ab", "abcd", "a"]
# key should get only 1 value and return only one value
print(sorted(lst, key=len))

print(sorted(lst, key=lambda x: x[0]))


books = (
    ("Book 1", 200),
    ("Book 2", 450),
    ("Book 3", 570),
    ("Book 4", 320),
)

print(sorted(books, key=lambda x: x[-1]))
