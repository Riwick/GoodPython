s = "pythony"

# str.method(args)

print(s.upper())
print(s.upper().lower())
print(s.count("y", 1))
print(s.count("t", 1, len(s)))

print(s.find("y", 2, len(s)))

# if not "abc" in str str.find == -1

print(s.rfind("y"))

# if not "abc" in str str.index - error
print(s.index("y"))

print(s.replace("y", "s"))
print(s.replace("y", "Y"))
print(s.replace("y", ""))
print(s.replace("y", "Y", 1), end="\n\n")

print(s.isalpha())

s_1 = "5.4"
print(s_1.isdigit())
s_1 = "54"
print(s_1.isdigit(), end="\n\n")

d = "abc"
print(d.rjust(5))

d = "12"
print(d.rjust(4, "0"))
print(d.rjust(1, "0"))
print(d.ljust(10, "*"), end="\n\n")

s = "Michal Jordan"
print(s.split(" "))

digs = "1, 2,3,  4,5,6"
print(digs.replace(" ", "").split(","))

res = digs.replace(" ", "").split(",")
print(", ".join(res))

name = "Michal Jordan"
print("\n".join(name.split()))

str_2 = "   hello world     \n"
print(str_2.strip())
print(str_2.rstrip())
print(str_2.lstrip())
