# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y(X, Y≤1000), а Катя должна их отгадать. Для этого Петя делает
# две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print('Введите сумму 2-х чисел --> ')
arg1 = int(input())
print('Введите произведение этих же 2-х чисел --> ')
arg2 = int(input())
print('Введите верхнюю границу поиска например 1000 --> ')
arg3 = int(input())


def ClueTwoNumbers(sum_numbers, multiply_numbers, final_numbers):
    x = 0
    while x <= final_numbers:
        x = x+1
        y = 0
        while y <= final_numbers:
            y = y+1
            if (x + y == sum_numbers and x * y == multiply_numbers):
                return x,y
                
a,b=ClueTwoNumbers(arg1, arg2, arg3)

print(f'Петя загадал цифры {a} и {b}')
print(f"проверка --> {a} + {b} = {arg1}, {a}x{b}= {arg2}")
