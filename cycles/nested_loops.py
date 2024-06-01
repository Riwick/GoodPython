"""
for <variable> in <iterable_object>:
    for <variable> in <iterable_object>:
        <operator_1>
        <operator_2>
        <operator_n>

while <condition>:
    while <condition>:
        <operator_1>
        <operator_2>
        <operator_n>

for <variable> in <iterable_object>:
    while <condition>:
        <operator_1>
        <operator_2>
        <operator_n>

while <condition>:
    for <variable> in <iterable_object>:
        <operator_1>
        <operator_2>
        <operator_n>
"""

for i in range(1, 4):
    for j in range(1, 6):
        print(f"{i=} {j=}", end=", ")
    print()

a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

for i in a:
    for j in i:
        print(j, end=" ")
    print()

b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
c = []

for index, row in enumerate(a):
    r = []
    for el_index, el_value in enumerate(row):
        r.append(el_value + b[index][el_index])
    c.append(r)

print(c)

t = ["adc adcs ", "bcd   gase", "dde advv  ", "resew", "geew   "]

for i, line in enumerate(t):
    while line.count("  "):
        line = line.replace("  ", " ")
    t[i] = line

print(t)


M, N = list(map(int, input("M and N: ").split()))

zeros = []
for i in range(M):
    zeros.append([0] * N)

print(zeros)

for i in range(M):
    for j in range(N):
        zeros[i][j] = 1

print(zeros)

A = [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]
                    ]


for i in range(len(A) - 1):
    for j in range(i + 1, 4):
        A[i][j], A[j][i] = A[j][i], A[i][j]


for r in A:
    for x in r:
        print(x, end="\t")
    print()

P = [[1],
                      [1, 1],
                      [1, 2, 1],
                      [1, 3, 3, 1],
                      [1, 4, 6, 4, 1],
                      [1, 5, 10, 10, 5, 1]]

N = 7

new_p = []
for i in range(1, N):
    new_p.append([1] * i)

for i, lst in enumerate(new_p):
    if i == 0 or i == 1:
        continue

    for j in range(1, len(lst) - 1):
        lst[j] =  new_p[i-1][j-1] + new_p[i-1][j]

for r in new_p:
    print(r)
