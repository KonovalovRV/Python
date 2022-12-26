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

print('Введите размер первого массива -- >  ')
len = int(input())
print('Введите размер второго массива -- >  ')
leng = int(input())

list = []
list1 = []


def print_array(array, length):
    for num in range(1, length):
        random_number = random.randrange(1, 20)
        array.append(random_number)
    print(array)


def array_identical_value(array1, array2):
    list4 = []
    for num in array1:
        for num1 in array2:
            if num == num1:
                list4.append (num)
        return list4       
        break


def print_arr(array10):
    for i in array10:
        print (array10)
  


    


# def array_increasing_value(array3):
#     list4 = []
#     for num in array3:
#         if num == num:
#             list4.append(num)
#                 break
#     print(list4)






print('Первый набор чисел')
print_array(list, len)
print('Второй набор чисел')
print_array(list1, leng)
print('Значения из обоих массивов')
a=array_identical_value(list, list1)
# dell_value(a)
print_arr(a)
