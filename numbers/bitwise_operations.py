a = 121

print(bin(a))
print(~a)  # not

d = 0
print(~d)

d = 10
print(~d)

d = -9
print(~d)

x1 = 1
x2 = 0
print(x1 & x2)  # and

x1 = 1
x2 = 1
print(x1 & x2)

flags = 5  # 00000101
mask = 4  # 00000100
res = flags & mask
print(res)

flags = 13
mask = 5
print(flags & ~mask)  # ~ has more priority

flags = 8
mask = 5
print(flags | mask)  # or

flags |= mask
print(flags)

flags = 9
mask = 1
print(flags ^ mask)  # xor

flags = 9
mask = 1
flags ^= mask
print(flags)
flags ^= mask
print(flags)  # value returns

"""
priority:
~ - 3 # not
& - 2 # and
| - 1 # or
^ - 1 # xor
"""

x = 160
print(bin(x))
x = x >> 1  # bit offset
print(x, bin(x))  # it's like x / 2

x = x >> 2
print(x, bin(x))  # it's like x / 4

x = 5
x = x >> 1
print(x, bin(x))  # it's like 5 // 2

x = 5
x = x << 1
print(x, bin(x))  # it's like 5 * 2

x = 5
x = x << 3
print(x, bin(x))  # it's like 5 * 8

"""
x = x >> 2 is faster than x / 4
"""