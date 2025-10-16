a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if not a == b:
    if a > b:
        a , b = a, a 
    else:
        a , b = b, b
elif a == b:
    a = 0
    b = 0
print("A =", a, "B =", b)