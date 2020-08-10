# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input("Введите целое трёхзначной число: "))

first_num = a // 100
second_num = (a % 100) // 10
third_num = a % 10

print(f'Сумма цифр числа = {first_num + second_num + third_num}')
print(f'Произведение цифр числа = {first_num * second_num * third_num}')
