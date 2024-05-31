lst: list = [1, -54, 3, 23, 43, -45, 0]

lst.append(100)
print(lst)

a = lst.append(40)
print(a, lst)

lst.append(True)
lst.append([1, 2, 3])
print(lst)

lst.insert(3, -1000)
print(lst)

lst.remove(True)
print(lst)

lst.remove(True)
print(lst)

# lst.remove("not_in_list") - error

print(lst.pop())
print(lst.pop(4))

# lst.clear()
# print(lst)

b = lst.copy()
print(b)

b.pop()
print(b, lst)

c = lst[:]
c = list(lst)
print(c)

print(c.count(1))

c.append(1)
print(c.count(1))
print(c.count(True))
print(c.count("123"))

print(c.index(1), c)

c.append(1)
print(c)
print(c.index(1, 9))

print("hgad" in c)

c.reverse()
print(c)

c.sort()
print(c)

c.sort(reverse=True)
print(c)

print(sorted(c))