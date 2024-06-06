"""
isinstance(<object>, <data_type>)
"""

print(isinstance("123", str))
print(isinstance(123, int))
print(isinstance("123", int))
print(isinstance(123.5, int))

b = True
print(isinstance(b, bool))

print(isinstance(b, int))  # because True in bool == 1

print(type(b) == bool)
print(type(b) == int)
print(type(b) is bool)
print(type(b) in (bool, float, str))

# isinstance checks whether it belongs to a certain class

data = (4.5, 8.7, True, "book", 8, 10, -11, [True, False])


def get_sum(iterable):
    sum = 0
    for x in iterable:
        if isinstance(x, (float, int)):
            sum += x

    return sum


print(get_sum(data))


print(sum(filter(lambda x: isinstance(x, (float, int)), data)))  # True == 1
print(sum(filter(lambda x: type(x) in (float, int), data)))  # without True

a = 5.5
print(isinstance(a, int) or isinstance(a, float))  # equals
print(isinstance(a, (int, float)))  # equals
