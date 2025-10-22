K = int(input("K = "))
N = 2 ** K

print('K = ', K)
print('N = ', N)

K_new = 0
while N >= 2:
    N /= 2
    K_new += 1
print("K = ", K_new)


