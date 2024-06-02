a = {1, 2, 3, "hello"}
print(a, type(a))

a = {1, 2, 3, "hello", 2, 3, "hello"}
print(a)

"""
only immutable types can be a set elements, like:
1) numbers
2) bools
3) strings
4) tuples
"""

a = {1, 1.4, "hi", (4, True)}
print(a)

# b = {[1, 2]} - error
# b = {{1: 1, 2: 2}} - error
# b = {{1, 2, 3}} - error

a = set()
print(a)

b = {}
print(type(b))

a = set([1, 2, 3, 4])
print(a)

a = set("python")
print(a)

a = set(range(7))
print(a)

# a[0] - error

lst = [0, 0, 0, 1, 2, 3, 3, 4, 4]
print(set(lst)) # only unique numbers
print(list(set(lst)))

q = set(lst)

for i in q:
    print(i, end=", ")

print()

it = iter(q)
print(next(it), next(it), next(it), next(it), next(it))

print(len(q))

q = {1, 2, 3, 4, 5}

print(1 in q)
print(max(q))
print(min(q))
print(sum(q)) # error if we try to plus str and int

b = set()
b.add(1) # add one element
print(b)
b.add(2)
b.add(3)
print(b)
b.add(3)
print(b)

b.update([4, 5, 6]) # add several elements
print(b)

b.update("python") # you can add any iterable object
print(b)

b.discard(2)
print(b)

b.discard("123") # no changes because "123" not in b
print(b)

b.discard(4)
print(b)

b.remove(3)
print(b)

# b.remove("123") - error because "123" not in b

b.pop() # delete random element
print(b)

b.pop()
print(b)

a = set()
# a.pop() - error because a is empty

b.clear()
print(b)
