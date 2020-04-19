def get_joint_cl(G, color, rand_state = const_rand):
    
    """
    Count joint partition
    G - list of adjacency matrixes
    color - list, where will be answer
    rand_state - random_state
    """
    
    ans = np.copy(color)
    
    while True:
        new_ans = get_joint_level(
            G, color, rand_state)
        #print(new_ans)
        if np.array_equal(ans, new_ans):
            return ans
        ans = new_ans