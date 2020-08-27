# Урок 3. Задача 5.
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
import sys

# Вариант 1
n = 10
arr = [random.randint(-100, 100) for _ in range(n)]
arr_neg = []  # отрицательные числа
for itm in arr:
    if itm < 0:
        arr_neg.append(itm)

max_neg_element = arr_neg[0]

for i in arr_neg:
    if i > max_neg_element:
        max_neg_element = i

print(max_neg_element)

# Выделение памяти
all_v = 0
for v in list(vars().keys()):
    if not v.startswith('_'):
        print(f'Переменная: {v}, Память: {sys.getsizeof(v)} байт(а)')
        all_v += sys.getsizeof(v)
print(f'Общая память: {all_v}')

# Вариант 2
n = 10
arr = [random.randint(-100, 100) for _ in range(n)]
i = 0
idx = -1

while i < n:
    if arr[i] < 0 and idx == -1:
        idx = i
    elif 0 > arr[i] > arr[idx]:
        idx = i
    i += 1

max_neg_element = arr[idx]

print(max_neg_element)

# Выделение памяти
all_v = 0
for v in list(vars().keys()):
    if not v.startswith('_'):
        print(f'Переменная: {v}, Память: {sys.getsizeof(v)} байт(а)')
        all_v += sys.getsizeof(v)
print(f'Общая память: {all_v}')

# Вариант 3
n = 10
arr = [random.randint(-100, 100) for _ in range(n)]
max_neg_element = float('-inf')
idx = -1

for i, itm in enumerate(arr):
    if 0 > itm > max_neg_element:
        max_neg_element = itm
        idx = i

print(max_neg_element)

# Выделение памяти
all_v = 0
for v in list(vars().keys()):
    if not v.startswith('_'):
        print(f'Переменная: {v}, Память: {sys.getsizeof(v)} байт(а)')
        all_v += sys.getsizeof(v)
print(f'Общая память: {all_v}')
