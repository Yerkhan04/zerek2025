n = int(input("n = "))
if n%2 == 0:
    L =2
else:
    L = 1

F = 1
while n>=L:
    F *= n
    n -= 2
print("F = ", F) 