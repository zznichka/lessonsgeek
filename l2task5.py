my_list =[9, 7, 6, 4, 4, 3]
print(f'Рейтинг в настоящее время: {my_list}')
new_numb = int(input('Введите число: '))
i = 0
for n in my_list:
    if new_numb <= n:
     i = i + 1
my_list.insert(i, new_numb)
print(my_list)

