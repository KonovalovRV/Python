# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


c = int(input('Введите число:  '))
d = int(input('Введите степень числа:  '))


def degree_number(a, b):
    if b == 0:
        return 1
    else:
        return a * degree_number(a, b-1)


print(degree_number(c, d))
