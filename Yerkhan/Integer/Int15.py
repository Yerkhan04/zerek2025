x = int(input())
x1 = x // 100
x2 = (x // 10) % 10
x3 = x % 10
new_number = x2 * 100 + x1 * 10 + x3
print(new_number)