a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
x = 0
y = 0
if a > 0:
    x += 1
else: 
    y += 1

if b > 0:
    x += 1
else:
    y += 1

if c > 0:
    x += 1
else:
    y += 1

print("Positive numbers:", x)
print("Negative numbers:", y)