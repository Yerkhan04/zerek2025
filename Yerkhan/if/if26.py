x = int(input())
if x <= 0:
    y = -x
elif 0 < x < 2:
    y = x ** 2
elif x >= 2:
    y = 4
print(x,y)