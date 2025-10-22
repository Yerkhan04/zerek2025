n = int(input())
s = 1
y = 1
for i in range(n):
    s +=0.1
    y *=s
print(round(y,3))