# задание 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

MIN_EL = -100
MAX_EL = 100
SIZE = 10

array = [random.randrange(MIN_EL, MAX_EL) for i in range(SIZE)]
print(array)


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        exchange_cnt = 0
        exchange_idx = len(arr) - 1
        for i in range(exchange_idx):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                exchange_cnt += 1
                exchange_idx = i  # иднекс, где произошла последняя перестановка
        if exchange_cnt == 0:
            return arr
        n += 1
    return arr


print(bubble_sort(array))
