K = int(input("K (1..365) = "))
const = 2 # 1 jan tuesday
names = {0: "воскресенье", 1: "понедельник", 2: "вторник",
         3: "среда", 4: "четверг", 5: "пятница", 6: "суббота"}
week = ((K + const - 2) // 7) + 1 
day = ((K - 1) + const) % 7
print("Week:", week)
print("Day:", names[day])

