# 4. Определить, какое число в массиве встречается чаще всего.

import random

array = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {array}')

count = 0
element = -1

for i in range(len(array)):
    count_new = array.count(array[i])
    if count_new > count:
        element = array[i]
        count = count_new

print(f'Число "{element}" встречается {count} раз(а)')
