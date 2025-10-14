x1 = int(input("Enter from 1 to 8 x1: "))
y1 = int(input("Enter from 1 to 8 y1: "))
x2 = int(input("Enter from 1 to 8 x2: "))
y2 = int(input("Enter from 1 to 8 y2: "))


if abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1 and not (x1 == x2 and y1 == y2):

    print("Кароль может ходить из клетки (x1,y1) в клетку (x2,y2) за один ход")
else:
    print("Кароль не может ходить из клетки (x1,y1) в клетку (x2,y2) за один ход")