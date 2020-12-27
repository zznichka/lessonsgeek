
def fact(number):
    f_num = 1
    for i in range(1, number + 1):
        f_num = f_num * i
        yield f'{i}! = {f_num}'


for el in fact(int(input('Вычислить факториал числа:  '))):
    print(el)