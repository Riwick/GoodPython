# list[start:stop:step]

lst = [1, 2, 3, 4, 5, 6]
print(lst[1:3])

a = lst[1:3]
a[1] = 4
print(a, lst)

print(lst[2:])
print(lst[:5])

nums = lst[:]
print(id(nums) == id(lst))

c = list(lst)
print(id(c) == id(lst))

d = lst
print(id(d) == id(lst))

marks: list = [2, 3, 4, 3, 5, 2]
print(marks[2:-1])
print(marks[-3:-1])

print(marks[1:5:2])
print(marks[:5:2])
print(marks[1::2])
print(marks[::2])
print(marks[::-1])
print(marks[5:1:-1]) # -1 in step args reverses list

marks[2:4] = ["good", "ok"]
print(marks)

marks[::2] = [0, 0, 0]
print(marks)

marks[2:4] = 10, 20
print(marks)

print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] != [1, 2, 3])
print([1, 2, 3] > [1, 2, 3])
print([10, 2, 3] > [1, 2, 3])
print([1, 2, 3, 4] >= [1, 2, 3])
print([1, 2, "abc"] > [1, 2, "abcd"])
# print([1, 2, 1] > [1, 2, "abcd"]) - error
