A = int(input())
B = int(input())
C = int(input())

N  = abs(A//C)*abs(B//C)
S = (A * B) - (N * C * C)
print (N, S)