N = int(input("N = "))
K = 1
while 3 **K < N:
    K += 1
K -=1
print(K)