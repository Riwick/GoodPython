file = open("files/file.txt", encoding="utf-8")

print(file.read(4))  # read only 4 symbols

print(file.tell())  # current cursor position by bytes
print(file.read())  # read all file from 5 symbol


file.seek(0)  # we drop cursor position
print(file.read())

print()
file.seek(0)
print(file.readline(), end="")  # we read all line
print(file.readline(), end="")

print()

file.seek(0)
for line in file:
    print(line, end="")

print()
print(file.tell())
file.seek(0)
print(file.tell())
print(file.readlines(), end="") # list

file.close() # close file
# file.close() set cursor position to 0
