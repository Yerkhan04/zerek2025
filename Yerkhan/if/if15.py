a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
summ=0
if a > b or a > c :
    if b > c:
        summ = a + b
    elif c > b:
        summ = a + c
if b > a or b > c :
    if a > c:
        summ = b + a  
    elif c > a:
        summ = b + c
if c > a or c > b:
    if a > b :
        summ = c + a
    elif b > a:
        summ = c + b
print(summ)
                
