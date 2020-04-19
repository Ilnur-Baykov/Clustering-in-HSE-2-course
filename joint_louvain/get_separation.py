def get_separation(
        G, color, sum_ins, sum_out, 
        tot_mas, ver_wei, rand_state = const_rand):

    """
    Find to which community we shuold add all vertices
    v - vertex, that we want to add
    G - adjacency matrix
    color - labels color
    sum_ins - sum of edges inside community
    sum_out - sum of edges outside community
    tot_mas - sum of all edges
    ver_wei - sum of edges, that are connected to vertices
    rand_state - random_state
    """

    random = np.random.RandomState(rand_state)
    rand_order = np.arange(len(color))
    new_ans = np.copy(color)
    random.shuffle(rand_order)
    for i in rand_order:
        remove_from(
            i, G, new_ans, sum_ins, 
            sum_out, tot_mas, ver_wei)
        to, k_in, k_out = get_best_modularity(
            i, G, new_ans, sum_ins, sum_out, 
            tot_mas, ver_wei)
        if to == -1:
            continue
        color_to = new_ans[to]
        new_ans[i] = color_to
        sum_ins[color_to] += k_in
        sum_out[color_to] += k_out
    return new_ans