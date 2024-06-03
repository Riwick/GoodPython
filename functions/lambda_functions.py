"""
lambda <params>: <commands>
"""

print(lambda x, y: x + y)
a = lambda x, y: x + y
print(a(1, 2)) # auto return

a = [4, 5, 6, lambda: print("lambda"), 7, 8]

a[3]()


lst = [5, 3, 0, -6, 8, 10, 1]


def get_filter(a, filter=None):
    if not filter:
        return a

    res = []
    for x in a:
        if filter(x):
            res.append(x)

    return res


print(get_filter(lst))
print(get_filter(lst, lambda x: x > 0)) # only positive numbers
print(get_filter(lst, lambda x: x % 2 == 0)) # only even numbers


# a = lambda a:
# print(a) - error

# lambda a: a = 1 - error

b = lambda a: a + 1
# b = lambda a: a += 1 - error

