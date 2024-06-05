"""
filter(<function>, <iterable_object>)
"""

a = filter(lambda x: x > 0, [x for x in range(-5, 6)])
print(a)  # filter object
print(next(a), next(a), next(a), next(a), next(a))


a = filter(lambda x: x > 0, [x for x in range(-5, 6)])
print(list(a))


def check_number(num):
    d = num - 1
    if d < 0:
        return False

    while d > 1:
        if num % d == 0:
            return False

        d -= 1
    else:
        return True


c = filter(check_number, [x for x in range(1, 11)])
print(list(c))


d = filter(str.isalpha, ["a", "ab1", "abc", "abcd23", "abcde"])
print(list(d))

# nested filter
c = filter(check_number, list(
    filter(lambda x: x > 0, [x for x in range(-10, 21)])))
print(list(c))


def check_number1(num):
    d = num - 1
    if d < 0 or num < 0:
        return False

    while d > 1:
        if num % d == 0:
            return False

        d -= 1
    else:
        return True


c = list(filter(check_number1, [x for x in range(-10, 21)]))
print(c)
