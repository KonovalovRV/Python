# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Bведите трехзначное число -->  ')
val = int(input())

def validate(arg):
    if arg < 100:
        print ('Введено не трехзначное число')
        return -1
    elif arg > 1000:
        print('Введено не трехзначное число')
        return -1
    else:
        return arg


vall = validate(val)


def sum_value_number(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum


value = sum_value_number(vall)
print(value)
