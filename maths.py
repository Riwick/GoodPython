import math

print(abs(-3.4)) # 3.4
print(abs(3.4)) # 3.4

a = abs(-3.5)
print(a)

print(min(10, 23, -3, 3, 42, 2, -100))

print(max(1, 3, 4, -5, 10, -32, 233))

print(pow(6, 2))
print(int(pow(49, 0.5)))
print(pow(27, 1/3))

print(round(0.5))
print(round(1.5))
print(round(10.5))
print(round(10.5000001))

print(round(7.3512, ndigits=2))
print(round(7.3566, ndigits=3))
print(round(7.3512, ndigits=-1))
print(round(712.3512, ndigits=-2))
print(round(712.3512, ndigits=-1))

# abs() min() max() pow() round()

print(max(1, 2, abs(-3), -10))
print(max(1, 2, abs(min(10, 5, -3)), -10))

print(math.ceil(3.5))
print(math.ceil(3.4))
print(math.ceil(-3.5))

print(math.floor(5.99))
print(math.floor(-5.99))

print(math.factorial(5))

print(math.trunc(5.8), int(5.8))

print(math.log2(4))
print(math.log10(100))
print(math.log(2.7))
print(math.log(27, 3))

print(math.sqrt(49))

print(math.e)
print(math.pi)
