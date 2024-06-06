import time


a = [True, True, True, True]
print(all(a))

a = [True, True, False, True]
print(all(a))  # return true if all elements are true

a = [0, 1, 2.5, "python", [], [1, 2], {}]
print(all(a))

print(bool(0), bool(1), bool(2.5), bool(
    "python"), bool([]), bool([1, 2]), bool({}))

# all elements in list interpreted to bool values

a = [1, 2.5, "python", [1, 2]]
print(all(a))


def all(iterable):  # custom all function
    all_res = True
    for x in iterable:
        all_res = all_res and bool(x)

    return all_res


print(all(a))

print()
a = [0, 1, 2.5, "python", [], [1, 2], {}]
print(any(a))  # return true if at least one element is true

print(any([False, False, False, False]))


def any(iterable):  # custom any function
    all_res = False
    for x in iterable:
        all_res = all_res or bool(x)

    return all_res


print(any(a))
print(any([False, False, False, False]))


P = [["0", "x", "x"], ["o", "x", "o"], ["x", "0", "x"]]


def check_time_exec(func):
    def wrapper(*args, **kwargs):
        first = time.time()
        res = func(*args, **kwargs)
        second = time.time()
        return res, f"{second - first:.6f}"

    return wrapper


@check_time_exec
def check_x(iterable):

    def true_x(x):
        return x == "x"

    for row in iterable:
        if all(map(true_x, row)):
            return True

    new_iterable = [el for row in iterable for el in row]

    col_1 = all(map(true_x, new_iterable[::3]))
    col_2 = all(map(true_x, new_iterable[1::3]))
    col_3 = all(map(true_x, new_iterable[2::3]))

    if col_1 or col_2 or col_3:
        return True

    diag_1 = all(map(true_x, new_iterable[::4]))
    diag_2 = all(map(true_x, new_iterable[2::2]))

    if diag_1 or diag_2:
        return True

    return False


print(check_x(P))


N = 10
P = ["0"] * (N ** 2)

P[4] = "*"

loss = any(map(lambda x: x == "*", P))
print(loss)
