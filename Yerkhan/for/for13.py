n = int(input())
s = 1 
y = 0
for i in range(n):
    s +=0.1 
    x = s * (-1)*(-1)**(i+1)
    y +=x
print(round(y,3))
