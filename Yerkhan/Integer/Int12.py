x = int(input())
x1 = x // 100
x2 = x // 10
x2_1 = x2 % 10
x3 = x % 10
new_number = x3 * 100 + x2_1 * 10 + x1
print(new_number)