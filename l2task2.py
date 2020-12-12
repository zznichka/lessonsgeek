my_list = list(input('Введите элементы списка: '))
i = 0
a = i + 1
while i + 1 < len(my_list):
    my_list.insert(i, my_list[i + 1])
    my_list.pop(i + 2)
    i = i + 2
print(my_list)

