a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

AB = abs(a - b)
AC = abs(a - c)

if AB < AC :
    print("Точка Б ближе к А", AB )
elif AB > AC :
    print("Точка С ближе к А", AC)