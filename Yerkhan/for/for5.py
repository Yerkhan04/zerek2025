x = int(input("Price of 1 kg: "))
n = 0

for i in range(0,10):
    n +=0.1
    y = x * n
    print(round(n,1), "kg = ", round(y,1))