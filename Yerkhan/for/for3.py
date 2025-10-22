a = int(input("a = "))
b = int(input("b = "))
n=0
for i in range(b-1, a, -1):
    n += 1
    print(i)
print("number of numbers n = ",n)