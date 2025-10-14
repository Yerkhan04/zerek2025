a = int(input())
b = int(input())
c = int(input())
a2 = a**2
b2 = b**2
c2 = c**2
print(a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2, "Треугольник со сторонами a,b,c является прямоугольным")