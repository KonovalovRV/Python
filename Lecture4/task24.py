# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только
# по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
# выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
# и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Input: 4
# (значения сгенерированы случайным образом
#  4 2 3 1)

# Output: 9

import random


def print_array(mass):
    for num in range(1, len+1):
        number_random = random.randrange(1, 25)
        mass.append(number_random)
    print(mass)


def quantity_berry_on_the_Bush(arr):
    max = 0
    i = 0
    sum = 0

    for i in arr:
        while count < 3:
            sum = sum + i
            if (sum > max):
                max = sum
        count = count + 1
    print(max)

    # while i < len.arr:
    #     count = 0
    #     if (len.arr - i < 3):
    #         break
    #     while count < 3:
    #         sum += arr[i]
    #         if (sum > max):
    #             max = sum
    #             count += 1


array = []
print('Введите количество кустов на грядке --->')
len = int(input())

print('Количество ягод на каждом кусте')
print_array(array)
quantity_berry_on_the_Bush(array)
# print(f'Максимальное количество ягод, которое можеть собрать модуль с куста и двух соседних с ним равно {num}')
