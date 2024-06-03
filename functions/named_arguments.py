def get_V(a, b, c):
    print(f"{a=}, {b=}, {c=}")
    return a * b * c


v = get_V(1, 2, 3)  # positional arguments
print(v)


v = get_V(b=1, a=2, c=3)  # named arguments
print(v)

# you need to write positional arguments first
v = get_V(1, c=2, b=3)
print(v)


def get_V2(a, b, c, verbose=True):  # formal parameter verbose
    if verbose:
        print(f"{a=}, {b=}, {c=}")
    return a * b * c


v = get_V2(1, 2, c=3)
print(v)

v = get_V2(1, 2, c=3, verbose=False)
print(v)


v = get_V2(1, 2, 3, False)
print(v)


def cmp_str(s1, s2, reg=False, trim=True):
    # s1 and s2 are actual parameters, reg and trim are formal parameters
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()

    return s1 == s2


print(cmp_str("Python ", " Python"))
print(cmp_str("python", "Python", reg=True))


def add_value(value, lst=[]):
    lst.append(value)
    return lst


print(add_value(1))
print(add_value(2))  # lst references on the same list after first call

print(add_value(1, []))
print(add_value(2, []))

print()


def add_value2(value, lst=None):  # immutable param as default to lst
    if not lst:
        lst = list()
    lst.append(value)
    return lst


print(add_value2(1))
print(add_value2(2))

l = add_value2(1)
l = add_value2(2, l)
print(l)


"""
def get_value(a, b) - actual parameters
def get_value(a=1, b=2) - formal parameters

get_value(1, 2) - positional arguments
get_value(a=1, b=2) - named arguments
"""
