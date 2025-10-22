import math
n = int(input())
num = 0
s = 0
for i in range(n):
    i += 1
    s = (2 * i - 1)
    num += s
kvad = math.sqrt(num)
print(num)
print(kvad)  