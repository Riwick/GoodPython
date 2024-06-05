
"""
(<variable> for <variable> in <iterabe_object>)
"""

a = (x ** 2 for x in range(5)) # this is not a tuple
print(a)

print(next(a), next(a), next(a), next(a), next(a)) # We can only go through the generator once
# next(a) - StopIteration

gen = (x ** 2 for x in range(6))

for x in gen:
    print(x)

#for x in gen:
#    print(x) - None


a = (x ** 2 for x in range(5))
print(list(a))

a = (x ** 2 for x in range(5))
print(set(a))
print(set(a)) # empty

print(sum((x ** 2 for x in range(6))))
print(max((x ** 2 for x in range(6))))


# print(list(range(100000000000000))) - MemoryError

gen = (x for x in range(100000000000000))

for i in gen:
    if i < 50:
        print(i, end=" ,")
    else:
        break


print()
a = (x for x in range(10, 19))
# print(len(a)) - error

print(len(list(a)))

print([(x for x in range(10, 19))]) # link to generator


a = (x for x in range(10, 19))
# print(a[0]) - error


a = (x ** 2 for x in range(5))

print(next(a))

print()

for x in [1, 2, 3]:
    print(x)

print()

print(next(a))