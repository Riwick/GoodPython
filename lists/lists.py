
print(["Moscow", "Tver", "Ufa"])

marks: list = [2, 3, 4, 5, 2, 3]
print(marks)
print(marks[0])
print(marks[1])

print(f"{sum(marks) / len(marks):.2f}")

print(marks[-1])
marks[0] = 3
print(marks[0])

marks[1] = "Ok"
print(marks)

lst = ["Moscow", 123, 2.3, True, [1, 2, 3], False]
print(lst)

a = []
b = list()
print(a, b, sep=", ")
b = list([True, False])
print(b)

print(list("python"))

print(len(marks))
print(len([]))

t = [23.5, 23.1, 3.6, 23.7]
print(min(t))
print(max(t))
print(sum(t), end="\n\n")

print(t)
print(sorted(t))
t_sort = sorted(t)
print(t, t_sort, sep=", ")
print(sorted(t, reverse=True))

words = ['cat', 'hamster', 'squirrel', 'rabbit']
sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)

numbers = [1, -2, 3, -4, -5]
print(sorted(numbers, key=lambda x: x * 2 == 2, reverse=True))

people = [
    {'name': 'Helen', 'age': 24},
    {'name': 'John', 'age': 21},
    {'name': 'Sam', 'age': 19}
   ]
sorted_people = sorted(people, key=lambda p: p['age'], reverse=True)
print(sorted_people)

s = list("python")
print(max(s))
print(min(s))
print(sorted(s), end="\n\n")
# print(sum(s)) - error

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] + [True, False])
print("I love python".split() * 2)
print(["I"] + ["love"] * 3 + ["python"], end="\n\n")

lst = [1, 232, 523, "Python", True]

print(232 in lst)
print([1, 2] in lst)

lst = [1, 232, 523, "Python", True, [1, 2]]
print([1, 2] in lst)
print("Python" in lst)

del lst[2]
print(lst)