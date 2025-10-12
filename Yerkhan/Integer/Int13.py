x = int(input())
x1 = x // 100
x2 = (x // 10) % 10
x3 = x % 10
new_number = x2 * 100 + x3 * 10 + x1
print(new_number)