x = int(input())
x1 = x // 100
x2 = (x // 10) % 10
x3 = x % 10
new_number = x1 * 100 + x3 * 10 + x2
print(new_number)