# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

import random
print('Введите размер массива --> ')
length = int(input())
print('Введите искомое значение в массиве --> ')
number = int(input())

array = []


def print_array(arr, len):
    for num in range(0, len):
        random_number = int(random.uniform(1, len/2))
        arr.append(random_number)
    print(arr)


def quantity_value_array(arr, value):
    count = 0
    i = 0
    for item in arr:
        if (arr[i] == value):
            count += 1
        i += 1
    print(count)


print('Массив')
print_array(array, length)
print('Количество искомых значений в массиве')
quantity_value_array(array, number)
