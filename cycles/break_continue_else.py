print("Start")

i = 0
while True:
    i += 1
    print(i)

    if i == 10:
        break

print("Stop")


d = [1, 5, 3, 6, 0, -4]
i = 0
fl_find = False

while i < len(d):
    print(i)

    if d[i] % 2 == 0:
        fl_find = True
        break

    i += 1

print(fl_find)


sum = 0
d = 1
while d != 0:
    d = int(input("d: "))
    if d % 2 == 0:
        continue

    sum += d
    print(f"sum = {sum}")


i = -10
sum = 0

while i < 10:
    if i == 0:
        print("It was broke")
        break # abnormal interruption

    sum += 1/i
    i += 1

else: # normal interruption
    print("Everything is good")


print(sum)