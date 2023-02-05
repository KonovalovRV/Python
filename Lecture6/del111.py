
# from os import system, name

# def clear():
#     if name == 'nt':
#         _ = system('cls')



print('Original')

mas = []
with open('file.txt', 'r+') as data:
    for line in data:
        mas.append(line.split(','))
print(mas)


print('Copy')

mass = []
with open('file.txt', 'r+') as data:
    for line in data:
        mass=data.read()
        print(mass)
     

list_new = []  
nam = input('Введите имя, фамилию или отчество ')
for user in mas:
    if (user[0] == nam) or (user[1] == nam) or (user[2] == nam):
        print(user)
        if input('Всё устраивает, контакт будет удален (Y/N)-->'):
            if 'Y': 
                del user[:]
                print('After delete')
                print (mas)
                with open('file.txt', 'w') as data:
                    res = ''.join(''.join(l) for l in mas)
                    print("res")
                    print (res)
                    data.writelines(res)
            if 'N': exit()

                  
# clear()





