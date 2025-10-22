n = int(input("n = "))
k = int(input("k = "))
r = n
q = 0
while r >= k:
    r = r - k
    q = q + 1
print("Частное = ", q)
print("Остаток = ", r)