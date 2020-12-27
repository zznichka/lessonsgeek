def fun(var_1, var_2):
    if var_2 == 0:
        print('На ноль делить нельзя!')
        return()
    else:
       result = var_1 / var_2
    return print(f"Частное от деления {var_1} на {var_2} равно {result}")
fun(int(input('Введите делимое: ')), int(input('Введите делитель: ')))


_____________________________

#Вот так не получилось, не могу понять,  почему:
def fun(var_1, var_2):
    try:
        var_2 = 0
    except ZeroDivisionError:
        print("error")
    result = var_1 / var_2
    return print(f"Частное от деления {var_1} на {var_2} равно {result}")
fun(int(input('Введите делимое: ')), int(input('Введите делитель: ')))