proseeds = int(input('Введите выручку:  '))
cost = int(input('Введите издержки:  '))
result = proseeds - cost
if result > 0:
    is_profit = True
else:
    is_profit = False
if is_profit:
    rent = proseeds / result * 100
    workers = int(input('Введите количество сотрудников   '))
    for_workers = result / workers

    print('Выручка составила: ', result)
    print('Выручка на сотрудника составила:  ', for_workers)

else:
    print('Вы работаете в убыток')