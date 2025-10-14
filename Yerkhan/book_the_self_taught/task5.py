rhymes = {"1" : "small", "2" : "blue", "3" : "tree", "4" : "door", "5" : "hive"}
n = input("Enter a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("No rhyme found")