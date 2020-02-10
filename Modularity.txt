def modularity(G, label_color, v, to_c2, C_tot, C_in, total_m):
    sum_in = C_in[to_c2]
    sum_tot = C_tot[to_c2]
    sum_k_v = 0
    sum_k_in = 0
    m_2 = 2 * total_m
    for i in range(len(G[v])):
        sum_k_v += G[v][i]
    for i in range(len(G[v])):
        if label_color[i] == to_c2:
            sum_k_in += G[v][i]
    first_st = (sum_in + 2 * sum_k_in) / m_2 - ((sum_tot + sum_k_v) / m_2)**2
    secon_st = sum_in / m_2 - (sum_tot / m_2)**2 - (sum_k_v / m_2)**2
    ans = first_st - secon_st
    return ans