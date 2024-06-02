a = {1, 2, 3}
b = {2, 3, 4}

print(a & b) # intersection

c = a & b
print(c)

a &= b
print(a)

c = {9, 10, 11}

print(a & c)

a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b)) # create a new set

a.intersection_update(b) # update the old set
print(a)

a = {1, 2, 3}
b = {2, 3, 4}

print(a | b) # unification

a |= b
print(a)

a = {1, 2, 3}

print(a.union(b), a)
c = a.union(b) # creating new set

a = {1, 2, 3}
b = {2, 3, 4}

print(a - b)
c = a - b # creating new set
print(c)

print(b - a) # it is important from which set the subtraction takes place
с = b - a
print(c, a, b)
print(a.difference(b))
a.difference_update(b)
print(a)


a = {1, 2, 3}
b = {2, 3, 4}

print(a ^ b) # unique elements from 2 sets
c = a ^ b
print(c)
print(a.symmetric_difference(b))
a.symmetric_difference_update(b)
print(a)

a = {1, 2, 3, 4, 5}
b = {2, 3, 4, 5, 6}

print(a == b)

a = {6, 5, 4, 3, 2}
b = {2, 3, 4, 5, 6}
print(a == b)

print(a != b)

a = {1, 2, 3, 4, 5, 6}
b = {2, 3, 4, 5, 6}

print(a > b)
print(b < a)

b.add(1)
print(a > b)
print(b > a)

"""
a & b, a.intersection(b) - intersection (elements which contains in both sets)
a | b, a.union(b) - unification (unique elements from first and second set)
a - b, a.difference(b) - difference (only unique elements from 1 set)
a ^ b, a.symmetric_difference(b) - symmetric difference (only unique elements from 2 sets)
"""
