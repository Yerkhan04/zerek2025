import math
A = float(input())
B = float(input())
C = float(input())
D = B**2-4*A*C
x1 = (-B - math.sqrt(D)) / (2*A)
x2 = (-B + math.sqrt(D)) / (2*A)
print(x1, x2)