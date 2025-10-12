x = int(input())
minutes = x // 60
hours = minutes // 60
N = x % 3600
print("Hours:", hours, "minutes:", minutes, "ostatok sec posle chasa:", N)