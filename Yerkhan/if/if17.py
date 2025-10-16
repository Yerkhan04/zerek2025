a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if  a < b < c or a > b > c:
    a = 2 * a
    b = 2 * b
    c = 2 * c
    print(a, b, c)
    
else:
    a, b, c = b, c, a 
    print(a, b, c )