# Домашнее задание Семинар 6
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# .
# Структура данных:
# Фамилия, имя, отчество, номер телефона.
# .
# Пример данных:
# Ivanov, Ivan, Ivanovich, +79111234567
# Petrov, Petr, Petrovich, +79119876543
# .
# Функции справочника:
# - Показать все записи
# - Найти запись по вхождению частей имени
# - Найти запись по телефону
# - Добавить новый контакт
# - Удалить контакт
# - Изменить номер телефона у контакта
# .
# Пример работы программы:
# .
# При запуске программы пользователю выдается меню:

# Введите номер действия:
# 1 - Показать все записи
# 2 - Найти запись по вхождению частей имени
# 3 - Найти запись по телефону
# 4 - Добавить новый контакт
# 5 - Удалить контакт
# 6 - Изменить номер телефона у контакта
# 7 - Выход

# После выбора действия выполняется функция, реализующая это действие.
# После завершения работы функции пользователь возвращается в меню.

import time
from os import system, name

text_1 = '''Номер действия:
1 - Показать все записи
2 - Найти запись по вхождению частей имени
3 - Найти запись по телефону
4 - Добавить новый контакт
5 - Удалить контакт
6 - Изменить номер телефона у контакта
7 - Выход'''

dictionary_txt = 'file.txt'


def clear():
    if name == 'nt':
        _ = system('cls')


def output_menu_dictionary(text):
    print(text)


def enter_name_user():
    name = input('Введите имя ')
    last_name = input('Введите фамилию ')
    middle_name = input('Введите отчество ')
    phone = input('Введите телефон ')
    list_0 = name, last_name, middle_name, phone
    return list_0

# 1


def tap_user_infomation():
    list_1 = []
    with open(dictionary_txt, 'r+') as data:
        for line in data:
            list_1.append(line.split(','))
        return list_1

# 2


def find_user_by_name(list_1):
    nam = input('Введите имя, фамилию или отчество ')
    for user in list_1:
        if (user[0] == nam) or (user[1] == nam) or (user[2] == nam):
            print(user[:])
    else:
        print('В справочнике нет такого человека')

# 3


def find_user_by_phone(list_1):
    number_phone = input('Введите номер телефона ')
    for user in list_1:
        if user[3] == number_phone + '\n':
            print(user[:])

# 4


def added_user(list_0):
    list_1 = []
    list_1 = ",".join(list_0)
    with open(dictionary_txt, 'a') as data:
        data.writelines('{}\n'.format(list_1))

# 5


def del_user(list_1):
    nam = input('Введите имя, фамилию или отчество ')
    for user in list_1:
        if (user[0] == nam) or (user[1] == nam) or (user[2] == nam):
            print(user)
            b = input('Всё устраивает, контакт будет удален (Y/N)-->')
            count = 0
            if b == 'Y':
                    del user[:]
                    list_2 = []
                    list_2 = list_1.copy()
                    with open('file.txt', 'w') as data:
                        data.writelines(''.join(','.join(l) for l in list_2))
            if b == 'N':
                count += 1
            if count < len(list_1):
                continue
            else:
                break


def change_user_phone(list_1):
    nam = input('Введите имя, фамилию или отчество ')
    for user in list_1:
         if (user[0] == nam) or (user[1] == nam) or (user[2] == nam):
            print(user)
            b = input('Устраивает? (Y/N)-->')
            count = 0
            if b == 'Y':
                a = input('Введите новый телефон-->')
                user[3] = f'{a}\n'
                list_3 = []
                list_3 = list_1.copy()
                with open('file.txt', 'w') as data:
                    data.writelines(''.join(','.join(l) for l in list_3))
            if b == 'N':
                count += 1
            if count < len(list_1):
                continue
            else:
                break


def menu(list_1, text):
    output_menu_dictionary(text)
    while (True):
        a = input('Введите номер действия:-->')
        if (a == '1'):
            print(list_1)
        if (a == '2'):
            find_user_by_name(list_1)
        if (a == '3'):
            find_user_by_phone(list_1)
        if (a == '4'):
            added_user(enter_name_user())
        if (a == '5'):
            del_user(list_1)
        if (a == '6'):
            change_user_phone(list_1)
        elif (a == '7'):
            exit()


clear()
print('Телефонный справочник')
f = tap_user_infomation()
menu(f, text_1)
