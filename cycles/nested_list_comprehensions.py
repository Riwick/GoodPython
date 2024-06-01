"""
[<value_formation>
    for <variable_1> in <iterable_object> if <condition>
    for <variable_2> in <iterable_object> if <condition>
    ...
    for <variable_N> in <iterable_object> if <condition>
]

for i in y:
    for j in i:
        <operations>
"""

a = [(x, y)
     for x in range(3) if x % 3 == 0
        for y in range(4) if y % 2 == 0]
print(a)

a = [f"{i} * {j} = {i * j}"
     for i in range(1, 4)
     for j in range(1, 4)]

print(a)

matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]]

a = [x
     for row in matrix
     for x in row]

print(a)

"""
[
    [<value_formation>
    for <variable> in <iterable_object>
    if <condition>]
    ] for <variable> in <iterable_object>
    if <condition>
]
"""

M, N = 3, 4
matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

B = [[x ** 2 for x in row] for row in A]
print(B)

a = [x ** 2
     for row in A
     for x in row
     ]

print(a)

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

t_a = [[row[i] for row in A] for i in range(len(A))]
print(t_a)

"""
[<value_formation> for <variable> in [<list_comprehension>] if <condition>]
"""

a = [x ** 2 for x in [y for y in range(5) if y % 2 == 0] if x == 2]
print(a)

a = [[i for i in [x for x in range(6)]] for z in range(6)]
print(a)