import time


def send_email(name, years):
    text = f"sending email to {name} which {years} years old"
    print(text)


send_email("Riwi", 18)


def get_sqrt(x):
    # local variable, you can't print it outside the function
    res = None if x < 0 else x ** 0.5
    return res, x  # equals to (res, x)

    return x  # this line was not executed
    print(x)  # this line was not executed too


a, b = get_sqrt(49)
print(a, b)


def get_max(x, y):
    return x if x > y else y


x, y, z = 5, 7, 10
print(get_max(x, get_max(y, z)))


def get_max_2(a, b, c):
    return get_max(a, get_max(b, c))


x, y, z = 5, 7, 10
print(get_max_2(x, y, z))


PERIMETR = True
if PERIMETR:
    def get_rect(a, b):
        return 2 * (a + b)
else:
    def get_rect(a, b):
        return a * b


print(get_rect(3, 5))


def get_rect(a, b): # type: ignore
    return 2 * (a + b)


def get_rect(a, b):
    return a * b


print(get_rect(3, 5))  # was called the second function


def even(x):
    return x % 2 == 0


for i in range(1, 19):
    if even(i):
        print(i, end=", ")


print()


x = -5
while x < 2:

    def get_number(x):
        return x

    print(get_number(x), end=",")
    x += 1


print()


x = -5
while x < 2:

    if x < -2:
        def get_number(x):
            return x
    else:
        def get_number(x):
            return x / 2

    print(get_number(x), end=",")
    x += 1


print()


# Example


def get_nod(a, b):
    """Calculation nod for a and b

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


print(get_nod(18, 24))
print(help(get_nod))


def test_get_nod(func):
    # --- test 1 ---
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("# test 1 - ok")
    else:
        print("# test 1 - failed")

    # --- test 2 ---
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("# test 2 - ok")
    else:
        print("# test 2 - failed")

    # --- test 3 ---
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st

    if res == 2:
        print("# test 2 - ok")
    else:
        print("# test 2 - failed")

    print(f"Execution time = {dt:.3f} sec.")


test_get_nod(get_nod)


def get_fast_nod(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


print(get_fast_nod(18, 24))


test_get_nod(get_fast_nod)
