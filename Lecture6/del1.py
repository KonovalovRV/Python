import os  # module
from os import system, name

# # sleep module to display output for some time period
# from time import sleep

# # define the clear function


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

# # print out some text
# print('Hello\n'*10)

# # sleep time 2 seconds after printing output
# sleep(5)

# # now call function we defined above


# with open(file_txt, "r+") as data:
#     data.write("hello world\n"*2)

# with open(file_txt, "r") as data:
#     print(data.read())

dictionary_txt = 'file.txt'


# def enter_name_user():
#     name = input('Введите имя ')
#     last_name = input('Введите фамилию ')
#     middle_name = input('Введите отчество ')
#     phone = input('Введите телефон ')
#     list_0 = [name, last_name, middle_name, phone]
#     return list_0


def tap_user_infomation():
    mas = []
    with open(dictionary_txt, 'r+') as data:
        for line in data:
            mas.append(line.split(','))
        return mas


# def added_user(list_0):
#     list_1 = ",".join(list_0)
#     with open(dictionary_txt, 'a') as data:
#         # for item in list_1:
#         data.writelines('{}\n'.format(list_1))


# def del_user():
# with open(dictionary_txt, 'r') as data:
#     list_new = data.readlines
# print(list_new)
# with open(dictionary_txt, 'a') as data_1:
list_1 = tap_user_infomation()
print(list_1)
nam = input('Введите имя, фамилию или отчество ')
for item in list_1:
    # if (item[0] == nam) or (item[1] == nam) or (item[2] == nam):
    if item [1] == nam:
        item.clear()
print(list_1.readlines)
# if input('Всё устраивает, контакт будет удален (Y/N): '):
#     if 'Y':
with open(dictionary_txt, 'a') as data:
    data.writelines('{}\n'.format(",".join(list_2)))
    # for user in list_1:
    #     data.writelines(user)


# print(list_1)
# del_user()

# added_user(enter_name_user())

