def my_func():
    sum = 0
    while True:
        user_numbers = input('Введите числа или нажмите Q для завершения:  ').split()
        for num in user_numbers:
            if num == 'Q':
                return sum
            else:
                try:
                    sum = sum + int(num)
                except ValueError:
                    print('данные введены неверно')
                    
        print(f'Сумма чисел равна {sum}')


print(my_func())