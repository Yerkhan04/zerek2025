try:
    a = input("Введите число:")
    b = input("Введите число:")
    a = int(a)
    b = int(b)
    print(a/b)
except(ZeroDivisionError, ValueError):
        print("Ошибка ввода")