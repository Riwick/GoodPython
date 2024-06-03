import time


def func_decorator(func):
    def wrapper(title):
        print("-- before func --")
        func(title)
        print("-- after func --")

    return wrapper


def some_func(title):
    print(f"some func {title}")


f = func_decorator(some_func)
f("Riwi")

print()
some_func = func_decorator(some_func)
some_func("Riwi")

print()


def func_decorator1(func):
    def wrapper(*args, **kwargs):
        print("-- before func --")
        res = func(*args, **kwargs)
        print("-- after func --")
        return res

    return wrapper


def some_func1(title, tag):
    print(f"some func {title=}, {tag=}")
    return f"<{tag}><{title}><{tag}>"


some_func = func_decorator1(some_func1)
print(some_func("Riwi", "tag"))


def exec_time_decorator(func):
    def wrapper(*args, **kwargs):
        dt = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        return res, f"exec_time={et-dt:.5f} sec."

    return wrapper


def get_nod(a, b): # type: ignore
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


get_nod = exec_time_decorator(get_nod)
print(get_nod(2, 1000000))


def fast_get_nod(a, b): # type: ignore
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


fast_get_nod = exec_time_decorator(fast_get_nod)
print(fast_get_nod(2, 1000000))

print()


@exec_time_decorator
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


@exec_time_decorator
def fast_get_nod(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


print(get_nod(2, 1000000), fast_get_nod(2, 1000000))
