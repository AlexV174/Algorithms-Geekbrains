# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

array = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {array}')

min_num = array[0]
max_num = array[0]

min_index = 0
max_index = 0

for i in range(len(array)):
    if i > 0:
        if array[i] < min_num:
            min_num = array[i]
            min_index = i
        if array[i] > max_num:
            max_num = array[i]
            max_index = i

print(f'Индекс минимального числа в массиве: {min_index}\nИндекс максимального числа в массиве: {max_index}')

array[min_index] = max_num
array[max_index] = min_num

print(f'Поменяли: {array}')
