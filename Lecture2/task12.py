# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y(X, Y≤1000), а Катя должна их отгадать. Для этого Петя делает
# две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print('Введите сумму 2-х чисел --> ')
arg1 = int(input())
print('Введите произведение этих же 2-х чисел --> ')
arg2 = int(input())


def ClueTwoNumbers(sum_numbers, multiply_numbers, final_numbers):
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    while x <= final_numbers:
        x += 1
        while y <= final_numbers:
            if (x + y == sum_numbers and x * y == multiply_numbers):
                x1 = x
                y1 = y
                y+=1
                break
    return (x1, y1)


(a, b) = ClueTwoNumbers(arg1, arg2)

print(f"{a}+{b}'='{arg1},{a}x{a}'='{arg2}")
