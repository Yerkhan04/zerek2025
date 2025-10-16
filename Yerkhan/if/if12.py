a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
min = 0
if a <= b and a <= c:
    min = a
elif b <= a and b <= c:
    min = b
elif c <= a and c <= b:
    min = c
print("Minimum value is:", min)