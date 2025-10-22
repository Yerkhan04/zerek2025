a = int(input("a = "))
n = int(input("n = "))
x = 1
sum = 0
for i in range(1, n + 1):
    x *= a * (-1)
    sum +=x
print(sum)