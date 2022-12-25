# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший
# по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6


import random
print('Введите размер массива --> ')
len = int(input())
print('Введите любое значение  --> ')
number = int(input())

array = []


def print_array(arr, leng):
    for num in range(0, leng):
        random_number = random.randrange(1, leng)
        arr.append(random_number)
    print(arr)


def find_number_befor_value(mas, value):
    for ite in mas:
        if ite == value-1:
            print(ite)
            break
        else:
            continue


def find_number_after_value(mas, value):
    for ite in mas:
        if ite == value+1:
            print(ite)
            break
        else:
            continue


print('Массив')
print_array(array, len)
print(f'Ближайшее значения к {number} в массиве')
# find_number_after_value(array, number)
find_number_befor_value(array, number)
find_number_after_value(array, number)
