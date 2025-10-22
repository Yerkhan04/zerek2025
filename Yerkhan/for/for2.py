import random

A = random.randrange(10)
n = random.randrange(10)+1
B = A + n
print('A = ', A)
print('B = ', B)

N = 0
for i in range(A,B+1,1):
    N +=1
    print(i," : ",N)
print("N = ",N)