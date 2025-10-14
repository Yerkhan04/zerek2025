qs = ["What is your name?", "How old are you?", "Where are you from?"]
n = 0
while True:
    print("Enter X to exit")
    a = input(qs[n])
    if a == "X":
        break
    n = (n + 1) % 3
