x1 = int(input("Enter from 1 to 8 x1: "))
y1 = int(input("Enter from 1 to 8 y1: "))
x2 = int(input("Enter from 1 to 8 x2: "))
y2 = int(input("Enter from 1 to 8 y2: "))
flag1 = False

if x1 == x2 or y1 == y2:
    flag1 = True
else:
    flag1 = False
print(flag1, "Фигура ладья может ходить из клетки (x1,y1) в клетку (x2,y2) за один ход")