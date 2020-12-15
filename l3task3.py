def my_func(var_1, var_2, var_3):
    sum = (var_1 + var_2 + var_3) - (min(var_2, var_3, var_1))
    return print(f"Сумма наибольших чисел {sum}")

num_1 = int(input('Введите число:'))
num_2 = int(input('Введите число:'))
num_3 = int(input('Введите число:'))


my_func(num_1, num_2, num_3)



