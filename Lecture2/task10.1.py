# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
# и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
print('Введите количество монет -->   ')
length = int(input())

array = []


def print_array(arr, len):
    for num in range(0, len):
        random_number = random.randrange(0, 2)
        arr.append(random_number)
    print(arr)


def sum_numbres_matrix(mat):
    i = 0
    summ = 0
    for item in mat:
        summ += item
    return summ


def least_quantity_coins(summ, len):
    if (len-summ == len/2):
        print(f'Можно превернуть любые {len/2} монет')
        return -1
    if (len-summ < len/2):
        print(f'Необходимо перевернуть {len-summ} монет с орлом')
        return -1
    if (len-summ > len/2):
        print(f'Необходимо перевернуть {summ} монет с решком')
        return -1


print('1 - монеты повернуты решком, 0 - монеты повернуты орлом')

print_array(array, length)

val = sum_numbres_matrix(array)

least_quantity_coins(val, length)
