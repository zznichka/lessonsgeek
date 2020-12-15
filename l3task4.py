def my_func(x, y):
    result = x ** y
    return print(result)
x = float(input('Введите число '))
y = int(input('Введите степень '))
if x < 0:
    print('некорректно введено число')
if y > 0:
    print('некорректная степень')


my_func(x, y)