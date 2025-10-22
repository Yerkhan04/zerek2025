x = int(input("Enter 1..999: "))

if x % 2 == 0:
    s = "четное"
else:
    s = "нечетное"

    i_str = str(x)
    n = len(i_str)
    if n == 1:
        s += " однозначное "
    elif n == 2:
        s += " двузначное "
    elif n == 3:
        s += " трехзначное "

print(s) 