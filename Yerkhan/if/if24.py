import math
x = int(input())
pi = 3.14
if x > 0:
    y = 2 * math.sin(x)
elif x <= 0:
    y = 6 - x
print(x, y)