s1 = "Панда"
s2 = "Панда 2"
print(s1, s2, end="\n\n")

s = "hello python"
print(s[0])

max_index = len(s) - 1
print(max_index)

print(s[-1], s[-2], sep="")

print("pandas"[3])

# string[start:stop]

print(s[1:3+1])
print(s[4:])
print(s[:5])
print(s[4::-1])
print(s[2:-2])

# string[start:stop:step]

print(s[2:10:2])
print(s[2::3])
print(s[:5:3])
print(s[::-1])

# s[0] = "H" - error
s2 = "H" + s[1:]
print(s2)