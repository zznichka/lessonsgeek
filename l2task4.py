words = input('Введите несколько слов через пробел:  ').split()
print(words)
for a, i in enumerate (words, 1):
    print(a, i) if len(i) <= 10 else print(a, i[:10])
