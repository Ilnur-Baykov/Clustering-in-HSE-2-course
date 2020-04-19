def get_new_level(
        G, color, sum_ins, 
        sum_out, tot_mas, ver_wei, rand_state = const_rand):

    """
    Count best partition
    G - adjacency matrix
    color - labels color
    sum_ins - sum of edges inside community
    sum_out - sum of edges outside community
    tot_mas - sum of all edges
    ver_wei - sum of edges, that are connected to vertices
    rand_state - random_state
    """

    ans = np.copy(color)
    while True:
        new_ans = get_separation(
            G, ans, sum_ins, 
            sum_out, tot_mas, ver_wei, rand_state)
        if np.array_equal(ans, new_ans):
            return ans
        ans = new_ans