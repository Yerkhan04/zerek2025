import math
a = int(input("a = "))
b = int(input("b = "))
y = 0
for i in range(a, b+1):
    x = math.sqrt(i)
    y +=x   
print(y)