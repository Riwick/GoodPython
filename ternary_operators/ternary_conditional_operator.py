a = 12
b = 7

# <variable> if <condition> else <variable>

res = a if a > b else b
print(res)

res = a + 2 if a > b else b - 5
print(res)

a = -12
b = -7

res = abs(a) if a > b else abs(b)
print(res)

res = print(a) if a > b else print(b)
print(res)

s = "python"
t = "upper"

res = s.upper() if t == "upper" else s
print(res)

a = 12
b = 7

lst = [1, 2, a if a < b else b, 4, 5]
print(lst)

s = f"a - {'четное' if a % 2 == 0 else 'нечетное'} число"
print(s)

print(max(1, 5, a if a > 0 else b, 4, 5))

a = 3
b = 5
c = 7

print(a if a > b else (b if b > c else c))