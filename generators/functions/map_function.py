"""
map(<function>, <iterable_object>)
"""

b = map(int, ["1", "2", "3", "4", "5"])
print(b) # returns map object like generator
print(next(b), next(b), next(b), next(b), next(b))


b = map(int, ["1", "2", "3", "4", "5"])
print(list(b))

b = (int(x) for x in ["1", "2", "3", "4", "5"])
print(list(b))


b = map(int, ["1", "2", "3", "4", "5"])
print(sum(b)) # max(), min()
print(sum(b))


c = map(lambda x: x > 0, [x for x in range(-5, 6)])
print(list(c))

c = map(len, ["a", "ab", "abc", "abcd"]) # only link to function without ()
print(list(c))


def get_upper_symbols(s):
    return list(s.upper())

d = map(get_upper_symbols, ["a", "ab", "abc", "abcd"])

print(list(d))

d = map(lambda s: list(s.upper()), ["a", "ab", "abc", "abcd"])
print(list(d))

d = list(map(lambda s: list(s.upper()), ["a", "ab", "abc", "abcd"]))
print(d)


s = list(map(int, input().split()))
print(s)
