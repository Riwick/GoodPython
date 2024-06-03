a = frozenset([1, 2, 3])
print(a)

# frozensets is immutable after create

# a.add(), a.discard(), a.remove(), a.update(), a.clear() - error

b = a.copy()
print(b)

a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

print(a | b)
print(a & b)
print(a ^ b)
print(a - b)

print()
print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.difference(b))

