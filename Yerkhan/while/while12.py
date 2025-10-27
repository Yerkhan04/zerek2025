N = int(input("N = "))
K = 0
summ = 0
while summ + (K + 1) <= N:
    K += 1
    summ += K 
    print(K)
print("summ = ", summ)
   