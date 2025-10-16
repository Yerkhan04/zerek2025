a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c more number: "))
flag = 0
if a < b or a < c:
    flag = a
    if b < c:
        flag = a, b ,c
        if c < b : 
            flag = a, c , b
if b < a or b < c:
    flag = b
    if a < c:
        flag = b, a , c
        if c < a : 
            flag = b, c , a
if c < b or c < a:
    flag = c
    if b < a:
        flag = c, a , b
        if a < b : 
            flag = c, a , b
print(flag)


