"""
{key: value, key: value,}

{
    key: value,
    key: value,
    key: value,
}
"""

d = {"house": "123", "car": "volvo", "tree": "1", "road": "is good"}
print(d)

print(d["house"], d["car"], d["tree"], d["road"])

d = {"house": 1, "house": 2}
print(d)

d = dict(one=1, two=2, three=3, four=4)
print(d)

# d = dict(1="23", two=2, three=3, four=4) - error

"""
as a dict-key you can't use a numbers
"""

lst = [[2, "bad"], [3, "ok"], [4, "good"], [5, "well"]]

d = dict(lst)
print(d)

d = dict()
print(d)
d = {}
print(type(d))

d[True] = "True"
print(d)
d[False] = "False"
print(d)

d[True] = 1
print(d)

# d[[1, 2]] = 1 - list is mutable type

d = {True: 1, False: "False", "list": [1, 2, 3], 5: 5}
print(d)

# as a value you can write any data type

print(len(d))

del d[5]
print(d, len(d))

# del d["abc"] - error

print("abc" in d)
# print([1, 2, 3] in d) - error
print("False" in d)

print("False" not in d)