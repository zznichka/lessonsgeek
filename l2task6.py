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