def get_joint_modularity(v, mat, index_sum, modul_sum):
    
    """
    Count all modularity for all matrix from vertex "v"
    v - vertex from we are going
    mat - list of matrix
    index_sum - index_sum
    modul_sum - modul_sum
    """
    
    G, color, tot_sum, sum_ins, sum_out, ver_wei = mat
    
    help_G = np.nonzero(G[v, :])[0]
    answer = np.zeros(len(help_G))
    if len(help_G) == 0:
        return
    for i in range(len(help_G)):
        to = help_G[i]
        modularity, k_in, k_out = add_to(
            v, to, G, color, sum_ins, 
            sum_out, tot_sum, ver_wei)
        index_sum[to] += 1
        modul_sum[to] += modularity
    return