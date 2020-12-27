start = int(input('Введите стартовое расстояние,км: '))
result = int(input('Введите желаемый результат,км: '))
day = 1
while start < result:
  start = start * 1.1
  day = day + 1
print(day)