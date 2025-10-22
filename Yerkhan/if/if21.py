x = int(input())
y = int(input())

if x == 0 and y == 0:
    print("0. Совпадает с началом координат")
elif y == 0:
    print("1. Лежит на оси OX")
elif x == 0:
    print("2. Лежит на оси OY")
else:
    print("3. Не лежит на координатных осях")