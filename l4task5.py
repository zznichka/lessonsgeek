from functools import reduce
list_2 = [num for num in range(100,1000,2)]
def my_func(prev_num, num):
    return prev_num * num
print(reduce(my_func, list_2))