# dictionary_txt = 'dictionary.txt'


# user_list_1 = [['ivan', 'ivanov', 'ivan', '7896644'], ['roman', 'konovalov', 'vadimovich', '89299801272']]

# user_list_2 = [['roman', 'konovalov', 'vadimovich',
                #  '89299801272'],['ivan', 'ivanov', 'ivan', '7896644']]
# user_list_2 = ivan, ivanov, ivan, 7896644

# ['ivan', 'ivanov', 'ivan', '7896644'],
# def enter_name_user():
#     name = input('Введите имя ')
#     last_name = input('Введите фамилию ')
#     middle_name = input('Введите отчество ')
#     phone = input('Введите телефон ')
#     name_list = [name, last_name, middle_name, phone]
#     # if " " in name_list:
#     print(name_list)

# def find_user_by_name(user_list):
#     nam = input('Введите имя ')
#     for user in user_list:
#         if user[0] == nam:         
#             # user.clear()
    


# enter_name_user()

# find_user_by_name(user_list_1)
# def enter_name_user():
#     name = input('Введите имя ')
#     last_name = input('Введите фамилию ')
#     middle_name = input('Введите отчество ')
#     phone = input('Введите телефон ')
#     name_list = name, last_name, middle_name, phone
#     return name_list


# t = enter_name_user()
# print(t)
# list=[]
# for i in t:
#     list = "". join(t)+'\n'
# print(list)
# print(list.split(','))   

# import os
# os.system('CLS')



# if os.path.exists('dict.txt'):
#     os.remove("dict.txt")
# else:
#   print("The file does not exist")


# my_list = [['a', 'b'], ['c', 'd']]

# result = ','.join(','.join(l) for l in my_list)

# print(result)


list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1)  # [12, 7, 11, -1, 21, 0]
