x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
flag1 = ""
flag2 = ""
if x1 % 2 == 1:
    if y1 % 2 == 1:
        flag1 = "черная"
    else:
        flag1 = "белая"

if x2 % 2 == 1:
    if y2 % 2 == 1:
        flag2 = "черная"
    else:
        flag2 = "белая"
print(flag1)
print(flag2)
print(flag1 == flag2, "Данные клетки одного цвета")