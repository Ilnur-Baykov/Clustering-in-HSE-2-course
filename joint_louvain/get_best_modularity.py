def get_best_modularity(
        v, G, color, sum_ins, 
        sum_out, tot_mas, ver_wei):

    """
    Find to which community we should add v
    v - vertex, that we want to add
    G - adjacency matrix
    color - labels color
    sum_ins - sum of edges inside community
    sum_out - sum of edges outside community
    tot_mas - sum of all edges
    ver_wei - sum of edges, that are connected to vertices
    """
    
    
    help_G = np.nonzero(G[v, :])[0]
    answer = np.zeros(len(help_G))
    if len(help_G) == 0:
        return v, 0, ver_wei[v]
    for i in range(len(help_G)):
        to = help_G[i]
        modularity, k_in, k_out = add_to(
            v, to, G, color, sum_ins, 
            sum_out, tot_mas, ver_wei)
        answer[i] = modularity
    if np.amax(answer) == 0:
        return -1, -1, -1
    result = np.where(answer == np.amax(answer))
    
    idi = random.randint(0, len(result[0]) - 1)
    
    to = help_G[result[0][idi]]
    mod, k_in, k_out = add_to(
        v, to, G, color, sum_ins, 
        sum_out, tot_mas, ver_wei)
    
    return to, k_in, k_out