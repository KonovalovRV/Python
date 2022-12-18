# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите размер шоколада в дольках по длине m= ')
seg_l = int(input())
print('Введите размер шоколада в дольках по ширине n= ')
seg_w = int(input())
print('Введите количество долек шоколада, которые необходимо отломить k= ')
seg = int(input())


def validate(m, n, k):

    if k >= m*n:
        return 1
    if k < n and k < m:
        return 1
    else:
        return k

def quatity_segment_chocolate(mm, nn, kk):
    if kk % mm == 0 or kk % nn == 0:
        return '--> yes'
    else:
        return '--> no'

segg = validate(seg_l, seg_w, seg)

d=quatity_segment_chocolate(seg_l, seg_w, segg)
print(d)