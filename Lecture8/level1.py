# Домашняя работа 8 Семинар
# Вычислить значение выражения
# Уровень 1:
# 1 действие
# 2 аргумента 12 + 15

# d = '12 * 15'




def split_expression(n):
    try:
        global a, b, c
        h = n.split()
        a = int(h[0])
        b = h[1]
        c = int(h[2])
        return (a, b, c)
    except ValueError:
        print("Не внимательно читаете!!!!!!")
    except IndexError:
        ("Выражение введено без пробелов")

def calc():
    try:
        if b == '+':
            return (a+c)
        if b == '-':
            return (a-c)
        if b == '/':
            return (a/c)
        if b == '*':
            return (a*c)
    except NameError:
        print("Выражение введено без пробелов")
    except IndexError:
        ("Выражение введено неправильно")
