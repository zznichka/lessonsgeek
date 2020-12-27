user_number = int(input('Введите число: '))
max = 0
if user_number > 0 :
    while user_number > 0:
        cut = user_number % 10
        if cut > max:
            max = cut
        user_number = user_number // 10
    print(max)
else:
    print ('error')