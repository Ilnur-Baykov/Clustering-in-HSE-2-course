def get_all_levels(G, color, sum_ins, 
        sum_out, tot_mas, ver_wei, rand_state = const_rand):
    
    """
    Count all levels of partition
    G - adjacency matrix
    color - labels color
    sum_ins - sum of edges inside community
    sum_out - sum of edges outside community
    tot_mas - sum of all edges
    ver_wei - sum of edges, that are connected to vertices
    rand_state - random_state
    """
    
    
    answer = get_new_level(
        G, color, sum_ins, 
        sum_out, tot_mas, ver_wei)
    while len(answer) != 1:
        index = {}
        for i in range(len(answer)):
            index[answer[i]] = index.get(answer[i], [])
            index[answer[i]].append(i)
        new_color = np.arange(len(index))
        n = len(new_color)
        
        
        dictionary = {}
        help_d = {}
        idi = 0
        for elem, lis in index.items():
            dictionary[idi] = dictionary.get(idi, lis)
            help_d[elem] = help_d.get(elem, idi)
            idi += 1
        
        new_G = np.zeros((n, n))
        for i in range(len(answer)):
            qwe = np.nonzero(G[i])
            indi = help_d[answer[i]]
            for j in qwe[0]:
                indj = help_d[answer[j]]
                if indi != indj:
                    new_G[indi][indj] += G[i][j]

        new_tot_mas = np.sum(new_G)
        new_sum_out = new_G.sum(axis = 1)
        new_sum_ins = np.zeros(len(new_G))
        new_ver_wei = new_G.sum(axis = 1)
        new_answer = get_new_level(
            new_G, new_color, new_sum_ins, 
            new_sum_out, new_tot_mas, new_ver_wei)
        print(dictionary)
        print()
        print(new_answer)
        print("_________________________")
        answer = new_answer
        color = new_color
        G = new_G
        tot_mas = new_tot_mas
        sum_out = new_sum_out
        sum_ins = new_sum_ins
        ver_wei = new_ver_wei
    
    return