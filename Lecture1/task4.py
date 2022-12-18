# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов
# сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10


birds_petya = 0
birds_kat = 0
birds_serg = 0

print('Введите количество журавликов - ->')

value = int(input())


def quantity_birds(value):

    birds_serg = value // 6
    birds_kat = 4 * birds_serg
    birds_petya = value // 6
    return (birds_serg,  birds_kat, birds_petya)


arg1, arg2, arg3 = quantity_birds(value)

print(f'{arg1} - {arg2} - {arg3}')
