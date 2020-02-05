import copy
import numpy



# Функция вычисляющая цвет через рандом
def func_rand(G, v, he, n, color, C_l):
    ans = 0
    tot_mas = 0.0
    mapp = [0] * (n + 1)
    for to in he:
        mas_of_child = G[v][to]
        col_of_child = C_l[to]
        #print(col_of_child, end = ' ')
        mapp[col_of_child] += mas_of_child
    vec = []
    for i in range(n + 1):
        if mapp[i] != 0:
            tot_mas += mapp[i]
        vec.append(i)
    #print(tot_mas)
    for i in range(n + 1):
        if mapp[i] != 0:
            mapp[i] /= tot_mas
    if tot_mas == 0:
        return color
    qwe = numpy.random.choice(vec, 1, p = mapp)
    ans = qwe[0]
    return ans



# Функция вычисляющая цвет через формулу
def func_math(G, v, he, n, color, C_l):
    ans = 0
    mx = -1
    mapp = [0] * (n + 1)
    for to in he:
        mas_of_child = G[v][to]
        col_of_child = C_l[to]
        mapp[col_of_child] += mas_of_child
    for i in range(1, n + 1):
        if mx < mapp[i]:
            mx = mapp[i]
    vec = []
    for i in range(1, n + 1):
        if mapp[i] == mx:
            vec.append(i)
    for i in vec:
        if color == i:
            ans = i
            break
    if ans != 0:
        return ans
    numpy.random.shuffle(vec)
    ans = vec[0]
    return ans



# Функция вычисляющая раскраску по func_math
def label_propagation(G, st_ver, n, h_G):
    rand_ver = [0] * n
    for i in range(n):
        rand_ver[i] = i
    update = True
    C = copy.deepcopy(st_ver)
    while update:
        update = False
        numpy.random.shuffle(rand_ver)
        for u in rand_ver:
            get_color = func_math(G, u, h_G[u], n, C[u], C)
            if get_color != C[u]:
                update = True
                C[u] = get_color
            
    return C


# Функция вычисляющая раскраску по func_rand
def label_propagation_rand(G, st_ver, n, h_G):
    rand_ver = [0] * n
    for i in range(n):
        rand_ver[i] = i
    update = 100
    C = copy.deepcopy(st_ver)
    while update > 5:
        update = 0
        numpy.random.shuffle(rand_ver)
        for u in rand_ver:
            get_color = func_rand(G, u, h_G[u], n, C[u], C)
            if get_color != C[u]:
                update += 1
                C[u] = get_color
            
    return C



# Ввод
n = int(input())
G = [];
help_G = []
for i in range(n):
    help_G.append([])
    G.append([int(j) for j in input().split()])
start_label = list(map(int, input().split()))


# Предподсчёт
mapp = [0] * (n + 1)
for i in start_label:
    mapp[i] += 1
id_i = 0
for i in range(1, n + 1):
    if mapp[i] == 0:
        id_i = i
        break
for i in range(n):
    if start_label[i] == 0:
        start_label[i] = id_i
        id_i += 1
        if id_i == n + 1:
            break
        while id_i != n + 1 and mapp[id_i] != 0:
            id_i += 1
for i in range(n):
    for j in range(len(G[i])):
        if G[i][j] != 0:
            help_G[i].append(j)



# Вычисление и вывод результата
get_ans = label_propagation(G, start_label, n, help_G)
for i in range(n):
    print(get_ans[i], end = ' ')





'''for i in range(n):
    for j in range(n):
        print(G[i][j], end = ' ')
    print()
for i in range(n):
    print(start_label[i], end = ' ')'''
