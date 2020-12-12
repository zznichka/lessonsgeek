my_list = [2, 3.8, 'добрый день', [4, 5], None, False]
i = 0
print(type(my_list))
while i < len(my_list):
    print(f'Тип элемента строки номер {i}', type(my_list[i]))
    i = i + 1

#2

my_list = list(input('Введите элементы списка: '))
i = 0
a = i + 1
while i + 1 < len(my_list):
    my_list.insert(i, my_list[i + 1])
    my_list.pop(i + 2)
    i = i + 2
print(my_list)


#3

number = int(input('Введите номер месяца: '))
if 0 < number < 12:
  season_list = ['зима', 'весна', 'лето', 'осень','зима']
  season_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
  print(f' Месяц номер {number} - это {(season_dict[number])}')
  print(f' Месяц номер {number} - это {season_list[number//3]}')
else:
  print('Номер месяца введен неправильно')


#4


words = input('Введите несколько слов через пробел:  ').split()
print(words)
for a, i in enumerate (words, 1):
    print(a, i) if len(i) <= 10 else print(a, i[:10])


#5

my_list =[9, 7, 6, 4, 4, 3]
print(f'Рейтинг в настоящее время: {my_list}')
new_numb = int(input('Введите число: '))
i = 0
for n in my_list:
    if new_numb <= n:
     i = i + 1
my_list.insert(i, new_numb)
print(my_list)


#6


general = []
catalog = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
  if input('Для выхода из программы нажите "Q", для продолжения нажите "Enter": ').upper() == 'Q':
      break
  num +=1
  for c in catalog.keys():
      new = input(f'Введите значение свойства {c}: ')
      catalog[c] = int(new) if c == 'цена' or c == 'количество' else new
      analytics[c].append(catalog[c])
  general.append((num, catalog))
  print(f'\nСтруктура товаров\n{general}')
  print(f'Текущая аналитика по товарам:\n')
  for key, value in analytics.items():
      print(f'{key}: {value}')









