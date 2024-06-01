d = [5, 3, 7, 10, 32]

print(iter(d))

it = iter(d)

print(next(it), next(it), next(it), next(it), next(it))

# print(next(it)) - StopIteration

it = iter(d)
print(next(it), next(it), next(it), next(it), next(it))

s = "python"

it = iter(s)
print(next(it), next(it), next(it), next(it), next(it), next(it))

# next(it) != s[n+1]

r = range(6)
it = iter(r)

print(next(it), next(it), next(it), next(it), next(it), next(it))

# "int" is not iterable

