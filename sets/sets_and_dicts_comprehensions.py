"""
[<value_formation> for <variable> in <iterable_object> if <condition>]

[<value_formation>
for <variable> in <iterable_object>
if <condition>]
"""

a = [x ** 2 for x in range(1, 5)]
print(a)

a = {x ** 2 for x in range(1, 5)}
print(a)

b = {x: x ** 2 for x in range(1, 5)}
print(b)

d = [1, 2, "1", "2", -4, 3, 4]
b = {int(x) for x in d} # it's faster than for cycle
print(b)

set_d = set()
for x in d:
    set_d.add(int(x))

print(set_d)

m = {"bad": "2", "ok": "3", "good": "4", "well": "5"}
d = {key.capitalize(): int(value) for key, value in m.items()}
print(d)

d = [1, 2, "1", "2", -4, 3, 4]
c = {int(x) for x in d if int(x) > 0}
print(c)

m = {"terrible": 0, "awful": 1, "bad": "2", "ok": "3", "good": "4", "well": "5"}

d = {int(key): value for value, key in m.items() if 2 <= int(key) <= 5}
print(d)



# if you can to replace a cycle by generator do it