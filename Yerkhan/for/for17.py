a = int(input("a = "))
n = int(input("n = "))
num = 0
x=1
sum = 0
total = 0
for i in range(1,n+1):
    num = i
    x = a**num
    sum +=x
total = 1 + sum
print(total)