K = int(input("K (1..365) = "))
N = int(input("N (1..7) = ")) # 1 jan tuesday
names = {0: "воскресенье", 1: "понедельник", 2: "вторник",
         3: "среда", 4: "четверг", 5: "пятница", 6: "суббота"}
week = ((K + N - 2) // 7) + 1 
day = ((K - 1) + N) % 7
print("Week:", week)
print("Day:", names[day])

