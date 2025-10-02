a = int(input("A: "))
b = int(input("B: "))
x, y = a, b
while y:
    x, y = y, x % y
print(a * b // x)   #a*b//gcd
