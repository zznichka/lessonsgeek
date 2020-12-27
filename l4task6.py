from itertools import count, cycle
for el in count(1):
    if el > 12:
        break
    else:
        print(el)
i = 0
seasons = ['winter', 'spring', 'summer', 'autumn']
for el in cycle(seasons):
    if i == 8:
        break
    print(el)
    i = i + 1
  