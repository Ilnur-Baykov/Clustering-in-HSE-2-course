def pre_calc(G, color):
    
    """
    Calculate tot_mas, sum_ins, sum_out, ver_wei 
    G - adjacency matrix
    color - labels color
    """
    
    tot_mas = np.sum(G)
    ver_wei = np.sum(G, axis = 1)
    
    n = len(set(color))
    sum_ins = np.zeros(n)
    sum_out = np.zeros(n)
    for i in range(len(color)):
        com_col = color[i]
        i_in = np.sum(G[i, np.where(color == com_col)])
        sum_ins[com_col] += i_in
        i_out = np.sum(G[i, np.where(color != com_col)])
        sum_out[com_col] += i_out
    sum_ins /= 2
    return tot_mas, sum_ins, sum_out, ver_wei