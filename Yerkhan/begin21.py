import math
xa = int(input())
ya = int(input())
xb = int(input())
yb = int(input())
xc = int(input())
yc = int(input())
a = math.sqrt((xc - xb) ** 2 + (yc - ya) ** 2)
b = math.sqrt((xc - xa) ** 2 + (yc - ya) ** 2)
c = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
P = a + b + c
s = (a + b + c) / 2
S = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(a, b, c, P, S)