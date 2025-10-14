x1 = int(input("Enter a number from 1 to 8: "))
y1 = int(input("Enter a number from 1 to 8: "))
x2 = int(input("Enter a number from 1 to 8: "))
y2 = int(input("Enter a number from 1 to 8: "))
print("Конь может ходить из клетки (x1,y1) в клетку (x2,y2) за один ход",
      (abs(x2 - x1) == 2 and abs(y2 - y1) == 1) or (abs(x2 - x1) == 1 and abs(y2 - y1) == 2))