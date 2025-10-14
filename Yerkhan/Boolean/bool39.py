x1 = int(input("Enter a number from 1 to 8: "))
y1 = int(input("Enter a number from 1 to 8: "))
x2 = int(input("Enter a number from 1 to 8: "))
y2 = int(input("Enter a number from 1 to 8: "))
print ("Ферзь может ходить из клетки (x1,y1) в клетку (x2,y2) за один ход", 
       x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1) and abs(x2 - x1) != 0)