N = int(input("Введите число N: "))
power = 1
result = False   
while power <= N:
    if power == N:
        result = True     # нашли, что N = 3ⁿ
        break             # можно остановить цикл
    power = power * 3     # увеличиваем степень 3

print(result)