# Задача 14
# Требуется вывести все целые степени двойки(т.е. числа вида 2 в степени k), не превосходящие числа N.
# 5
# 1 2 4
# 17
# 1 2 4 8 16

print('Введите цифру основание степени цифру {2} -->  ')
val = int(input())
print('Введите цифру для определения границы расчета -->  ')
num = int(input())


def DegreeOfCount(value, number):
    num1 = 0
    k = 0
    while num1 < number:
        num1 = pow(value, k)
        k += 1
        if num1 == num or num1 > num:
            return
        print(num1)

DegreeOfCount(val, num)

