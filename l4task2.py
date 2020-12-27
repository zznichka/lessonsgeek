my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
prev_num = my_list[0]
for num in my_list:
    if num > prev_num:
        new_list.append(num)
    prev_num = num
print(new_list)