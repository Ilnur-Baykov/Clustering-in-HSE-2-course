import numpy as np



def remove_from(v, G, Help_G, label_color, 
    Sum_inside, Sum_outside, Total_mass, Weight_of_ver):
    comm_color = label_color[v]
    k_v = Weight_of_ver[v]
    k_v_in = 0
    for i in Help_G[v]:
        if label_color[i] == comm_color:
            k_v_in += G[v][i]
    Sum_inside[comm_color] -= k_v_in
    Sum_outside[comm_color] -= (k_v - k_v_in)
    return



def add_to(v, to, G, Help_G, label_color, 
    Sum_inside, Sum_outside, Total_mass, Weight_of_ver):
    comm_color = label_color[to]
    sum_total = Sum_inside[comm_color] + Sum_outside[comm_color]
    k_v = Weight_of_ver[v]
    k_v_in = 0
    #print(label_color, comm_color, sep = " // ", end = " | ")
    for i in Help_G[v]:
        if (label_color[i] == comm_color):
            k_v_in += G[v][i]

    first = (k_v_in / Total_mass)
    second = (sum_total * k_v) / (2 * (Total_mass ** 2))
    add_ans = first - second
    k_v_out = k_v - k_v_in
    return add_ans, k_v_in, k_v_out



def get_best_modularity(v, G, Help_G, label_color, 
    Sum_inside, Sum_outside, Total_mass, Weight_of_ver):
    answer = np.zeros(len(Help_G[v]))
    if len(Help_G[v]) == 0:
        return v, 0, Weight_of_ver[v]
    for i in range(len(Help_G[v])):
        to = Help_G[v][i]
        modularity, k_in, k_out = add_to(v, to, G, Help_G, label_color, Sum_inside, Sum_outside, Total_mass, Weight_of_ver)
        answer[i] = modularity
    result = np.where(answer == np.amax(answer))
    to = int(Help_G[v][result[0][0]])
    mod, k_in, k_out = add_to(v, to, G, Help_G, label_color, Sum_inside, Sum_outside, Total_mass, Weight_of_ver)
    return to, k_in, k_out



def get_separation(n, G, Help_G, label_color, 
    Sum_inside, Sum_outside, Total_mass, Weight_of_ver):
    rand_order = np.arange(n)
    new_ans = np.copy(label_color)
    np.random.shuffle(rand_order)
    for i in rand_order:
        remove_from(i, G, Help_G, new_ans, Sum_inside, Sum_outside, Total_mass, Weight_of_ver)
        to, k_in, k_out = get_best_modularity(i, G, Help_G, new_ans, Sum_inside, Sum_outside, Total_mass, Weight_of_ver)
        color_to = new_ans[to]
        new_ans[i] = color_to
        Sum_inside[color_to] += k_in
        Sum_outside[color_to] += k_out
    #print(new_ans, end = " | ")
    return new_ans



def get_new_level(n, G, Help_G, label_color,
    Sum_inside, Sum_outside, Total_mass, Weight_of_ver):
    ans = np.copy(label_color)
    changed = 1
    while changed:
        new_ans = get_separation(n, G, Help_G, ans, Sum_inside, Sum_outside, Total_mass, Weight_of_ver)
        #print(ans, new_ans, (ans == new_ans), sep = " || ")
        if np.array_equal(ans, new_ans):
            changed = 0
        ans = new_ans
    return ans



# input
n = int(input())
G = np.empty((n, n))
Help_G = []
for i in range(n):
    Help_G.append([])
    G[i] = np.array([int(j) for j in input().split()])
label_color = np.arange(n)



#pre_calc
Total_mass = np.sum(G)
H_G = np.nonzero(G)
for i in range(len(H_G[0])):
    Help_G[H_G[0][i]].append(H_G[1][i])
Sum_outside = G.sum(axis = 1)
Sum_inside = np.zeros(n)
Size_of_comm = np.ones(n)
Modu_of_comm = np.zeros(n)
Weight_of_ver = G.sum(axis = 1)



#get_ans
answer = get_new_level(n, G, Help_G, label_color, Sum_inside, Sum_outside, Total_mass, Weight_of_ver)
print(answer)
