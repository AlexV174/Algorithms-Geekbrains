# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран

import timeit
import cProfile


def renum1(num):
    n = str(num)
    s = 0
    for i, el in enumerate(n):
        s += int(el) * 10 ** i
    return s


print(renum1(122345))

print(timeit.timeit('renum1(123)', number=100, globals=globals()))  # 0.0001221999999999994
print(timeit.timeit('renum1(123456)', number=100, globals=globals()))  # 0.00021909999999999985
print(timeit.timeit('renum1(123456789876)', number=100, globals=globals()))  # 0.00044319999999999776
print(timeit.timeit('renum1(123456789876543210123456)', number=100, globals=globals()))  # 0.0009594999999999985


def renum2(num):
    n = 1
    while num // n > 10:
        n *= 10
    new_num = 0
    point = 1
    while n >= 1:
        new_num += num // n * point
        num -= num // n * n
        point *= 10
        n /= 10
    return int(new_num)


print(renum2(12345))

print(timeit.timeit('renum2(123)', number=100, globals=globals()))  # 0.00013670000000000002
print(timeit.timeit('renum2(123456)', number=100, globals=globals()))  # 0.00026419999999999916
print(timeit.timeit('renum2(123456789876)', number=100, globals=globals()))  # 0.0006232000000000008
print(timeit.timeit('renum2(123456789876543210123456)', number=100, globals=globals()))  # 0.0013127999999999994


def renum3(num):
    num = str(num)
    new_num = ''
    index = len(num)
    while index > 0:
        new_num += num[index - 1]
        index -= 1
    return int(new_num)


print(renum3(12345))

print(timeit.timeit('renum3(123)', number=100, globals=globals()))  # 7.180000000000034e-05
print(timeit.timeit('renum3(123456)', number=100, globals=globals()))  # 0.00010560000000000083
print(timeit.timeit('renum3(123456789876)', number=100, globals=globals()))  # 0.00017489999999999867
print(timeit.timeit('renum3(123456789876543210123456)', number=100, globals=globals()))  # 0.00030929999999999847

cProfile.run('renum1(123456789876543210123456)')
cProfile.run('renum2(123456789876543210123456)')
cProfile.run('renum3(123456789876543210123456)')
