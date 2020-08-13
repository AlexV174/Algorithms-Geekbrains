# 5.Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.

def ascii_symbols(a, b):
    sequence = range(a, b + 1)
    string = ''
    count = 0
    for i in sequence:
        string = string + str(f'{i}-"{chr(i)}" ')
        count += 1
        if count == 10:
            print(string)
            count = 0
            string = ''


a = 32
b = 127
ascii_symbols(a, b)
