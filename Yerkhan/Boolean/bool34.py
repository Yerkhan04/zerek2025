x1 = int(input())
y1 = int(input())
flag1 = ""

if x1 % 2 == 1:
    if y1 % 2 == 1:
        flag1 = "черная"
    else:
        flag1 = "белая"

print(flag1)
print(flag1 == "белая", "Данная клетка белая")