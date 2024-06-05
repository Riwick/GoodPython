import sys
import time


def get_list():
    for x in [1, 2, 3, 4, 5]:
        yield x  # return numbers step by step


a = get_list()
print(next(a), next(a), next(a), next(a), next(a))

a = get_list()
for x in a:
    print(x)


"""
generator returns only iterator without next() function
"""


def get_number():
    for i in range(1, 10):
        a = range(i, 10)
        yield sum(a) / len(a)


a = get_number()
print(list(a))


def find_word(f, word):
    g_indx = 0
    for line in f:
        indx = 0
        while (indx != -1):
            indx = line.find(word, indx)
            if indx > -1:
                yield g_indx + indx
                indx += 1

        g_indx += len(line)


try:
    with open("generators\\lesson_54.txt") as file:
        a = find_word(file, "generator")
        print(list(a))

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Some error", e)


print()

a = (x ** 2 for x in range(6))


def get_gen_number():
    # yield from <another_generator>
    yield from a  # yield value from other generator


print(list(get_gen_number()))
print()


def get_gen_number2():
    a = (x ** 3 for x in range(1, 31))
    yield from a


print(list(get_gen_number2()))


def get_gen_number3():
    a = (x ** 3 for x in range(1, 31))
    b = (x ** 3 for x in range(2, 32))
    yield from a # yield from returns only one generator
    yield from b


def get_generators():
    a = (x ** 3 for x in range(1, 31))
    b = (x ** 3 for x in range(2, 32))
    yield from (a, b) # it's yield tuple from 2 generators


print(list(get_generators()))
