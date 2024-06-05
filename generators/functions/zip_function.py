"""
zip(<iterable_objects>)
"""

z = zip([x for x in range(6)], [x for x in range(12) if x % 2 == 0])
print(z) # zip object
print(next(z), next(z), next(z), next(z), next(z), next(z))


print()

z = zip([x for x in range(6)], [x for x in range(12) if x % 2 == 0])
for x in z:
    print(x)

# print(next(z)) - stop iteration

z = zip([x for x in range(6)], [x for x in range(12) if x % 2 == 0])
z = tuple(z) # if tuple we can iterate many times

print()
for x in z:
    print(x)

for x in z:
    print(x)


print()

c = "python"

z = zip([x for x in range(6)], [x for x in range(12) if x % 2 == 0], c)
# print(list(z))


for v1, v2, v3 in z:
    print(v1, v2, v3)


print()
z1, z2, z3, z4, z5, z6 = zip([x for x in range(6)], [x for x in range(12) if x % 2 == 0], c)
print(z1, z2, z3, z4, z5, z6)

print()
z1, *z2 = zip([x for x in range(6)], [x for x in range(12) if x % 2 == 0], c)
print(z1, z2)
print(z1, *z2)

print(tuple(zip(*z2)))

print()
z = zip([x for x in range(6)], [x for x in range(12) if x % 2 == 0], c)
print(tuple(zip(*z)))

