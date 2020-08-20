import math
import timeit
import cProfile


def test_func(func):  # функция для проверки работоспособности функций
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    for i, item in enumerate(lst):
        assert item == func(i + 1)
        print(f'Test {i + 1} OK')


def numbers_required(num):  # функция, вычисляющая сколько  натуральных чисел нужно взять для поиска num простых чисел
    if num < 3:
        return 4
    n = num * math.log(num)
    if num < 4:
        n *= 2
    elif num <= 7:
        n *= 1.5
    elif num < 100:
        n *= 1.3
    elif num < 1000:
        n *= 1.2
    elif num < 10000:
        n *= 1.14
    elif num < 100000:
        n *= 1.13
    elif num < 1000000:
        n *= 1.121
    return int(round(n))


def sieve(num):  # алгоритм Решета Эратосфена
    n = numbers_required(num)
    a = [0] * n
    for i in range(n):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    return b[num - 1]


def my_func(num):  # алгоритм поиска простых чисел перебором
    if num < 3:
        return num + 1
    el = 2
    i = 1
    while i < num:
        el += 1
        for n in range(el, 2, -1):
            if el % (n - 1) == 0:
                i -= 1
                break
        i += 1
    return el


test_func(sieve)
test_func(my_func)

print(sieve(60))
print(my_func(60))