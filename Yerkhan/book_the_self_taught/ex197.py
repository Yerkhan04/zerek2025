tv = ["Breaking Bad", "Game of Thrones", "The Office", "Stranger Things"]
i = 0
for show in tv:
    new =tv[i]
    tv[i] = new.upper()
    i += 1
print(tv)