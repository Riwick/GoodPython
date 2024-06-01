# n = int(input("n: "))

# if 1 < n < 100:
#     sum = 1
#     for i in range(1, n + 1):
#         sum *= i

#     print(f"{n}! = {sum}")
# else:
#     print("Wrong number")


for i in range(1, 14):
    if i % 2 == 0:
        continue

    print(f"{'*' * i:^14}")


words = ["python", "like", "variable", "list", "iterator"]

s = ""
for w in words:
    s += f" {w}"

print(s.strip())

s = " ".join(words)
print(s)

digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i in range(len(digs)):
    if 10 <= abs(digs[i]) <= 99:
        digs[i] = 0

print(digs)


digs = [4, 3, 100, -53, -30, 1, 34, -8]

for index, value in enumerate(digs):
    if 10 <= abs(value) <= 99:
        digs[index] = 0

print(digs)

