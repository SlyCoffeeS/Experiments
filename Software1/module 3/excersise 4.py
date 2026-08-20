import math

a, b, c = input('Give me three integer numbers').split()
a = float(a)
b = float(b)
c = float(c)

sum = a + b + c
product = a * b * c
average = (a + b + c) / 3

print(f"Sum:", sum, "product:", product, "average:", average )