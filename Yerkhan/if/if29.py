x = int(input())
if x > 0 and x%2 == 0:
    print("Положительное четное число")
elif x == 0:
    print("Нулевое число")
elif x < 0 and x%2 == 1:
    print("Отрицательное нечетное число")