# Задача 22:
# Даны два неупорядоченных набора целых чисел(может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
#  2 4 6 8 10 12 10 8 6 4 2
#  3 6 9 12 15 18)
# Output: 11 6
# 6 12

import random

print('Введите размер первого множества чисел -- >  ')
leng_1 = int(input())
print('Введите размер второго множества чисел -- >  ')
leng_2 = int(input())

a = set()
b = set()
list = []


def print_set(array, length):
    for num in range(0, length+1):
        random_number = round(random.randrange(1, 100))
        array.add(random_number)
    print(array)

def intersection_set(set_1, set_2):
    c = set_1.intersection(set_2)
    return c

def transfer_from_set_to_list(set, list4):
    for num in set:
        list4.append(num)
    return list4

def location_increasing_value(list_1):
    for i in range(len(list_1)):
        max = list_1[0]
        for i in range(len(list_1)):
            temp = 0
            if list_1[i] < max:
                temp = list_1[i]
                list_1[i] = max
                max = temp
            else:
                continue
    print(list_1)

print('Первый набор чисел')
print_set(a, leng_1)
print('Второй набор чисел')
print_set(b, leng_2)
f = intersection_set(a, b)

t=transfer_from_set_to_list(f, list)

print('Общие значение для обоих множеств')
location_increasing_value(t)
