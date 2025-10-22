n = int(input("N = "))
num = 0
x = 1
summ = 0
for i in range(1, n+1):
    num = i
    x *=num
    print("x = ", x)
    summ += x
    print("sum", summ)

