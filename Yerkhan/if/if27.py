x = int(input())

if x < 0:
    y = 0
elif x%2 == 0:
    y = 1
else:
    y = -1
print(x, y)