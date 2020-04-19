def get_joint_level(G, color, rand_state = const_rand):
    
    """
    Find to which community we shuold add all vertices
    G - list of adjacency matrixes
    color - list, where will be answer
    rand_state - random_state
    """
    
    random = np.random.RandomState(rand_state)
    rand_order = np.arange(len(color))
    new_ans = np.copy(color)
    random.shuffle(rand_order)
    #print(G[0][1], sep = " ~ ")
    for i in rand_order:
        index_sum = np.zeros(len(color))
        modul_sum = np.zeros(len(color))
        v = i
        for mat in G:
            remove_from(v, mat[0], mat[1], mat[3], 
                mat[4], mat[2], mat[5])
            get_joint_modularity(v, mat, index_sum, modul_sum)
        to = joint_func(index_sum, modul_sum)
        if to == -1:
            continue
        #print(v, to, end = " | ")
        for mat in G:
            M, label, tot_sum, sum_ins, sum_out, ver_wei = mat
            mod, k_in, k_out = add_to(
                v, to, M, label, sum_ins, 
                sum_out, tot_sum, ver_wei)
            color_to = label[to]
            label[v] = color_to
            sum_ins[color_to] += k_in
            sum_out[color_to] += k_out
    new_ans = G[0][1]
    return new_ans