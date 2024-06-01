"""
while <condition>: - heading
    <operator_1>
    <operator_2> - body
    <operator_n>
"""

s = 0
i = 1
N = 1000

while i <= 1000:
    s += i # iteration
    i += 1

print(s)

s = 0
i = 1

while i <= N and i <= 50:
    s += i
    i += 1

print(s)


s = 0
i = 1

while i <= N and i <= 50:
    if i % 2 == 1:
        s += i
    i += 1

print(s)

i = 0
while i < 10:
    print(i)
    i += 1

i = 0
while i > -20:
    print(i)
    i -= 1

pass_true = "password"
ps = ""

while ps != pass_true:
    ps = input("Password: ")

print("Good")

N = 20
i = 1

while i <= N:
    if i % 3 == 0:
        print(i)

    i += 1
