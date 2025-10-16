a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
if  a > b > c or a < b < c:
    print(b)
elif b > a > c or b < a < c:
    print(a)
elif c > a > b or c < a < b:
    print(c)