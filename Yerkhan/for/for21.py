n = int(input())
summ = 0
num = 0
y = 0
x=1
z= 0
for i in range(1, n+1):
    num = i
    x *= num
    y = (1/x)
    z += y
print(z+1)