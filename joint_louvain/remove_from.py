def remove_from(
        v, G, color, sum_ins, 
        sum_out, tot_mas, ver_wei):
    
    """
    Remove vertex from community
    v - vertex
    G - adjacency matrix
    color - labels color
    sum_ins - sum of edges inside community
    sum_out - sum of edges outside community
    ver_wei - sum of edges, that are connected to vertices
    """

    
    com_col = color[v]
    k_v = ver_wei[v]
    k_v_in = np.sum(G[v, np.where(color == com_col)])
    sum_ins[com_col] -= k_v_in
    sum_out[com_col] -= (k_v - k_v_in)
    return