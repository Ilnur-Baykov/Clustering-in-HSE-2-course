def generate_graphs_without(G, dell, non_z, num, pod_mat):
    
    """
    Generate matrices without some edges
    Returns list - np.array of matrices
    G - adjacency matrix
    dell - list of edges
    non_z - indeces of non zero edges
    num - number of edges, that we want to delete
    pod_mat - how many matrices we want to generate
    """
    
    mats = []
    for j in range(pod_mat):
        qwe = random.sample(list(dell), num)
        H = deepcopy(G)
        for el in qwe:
            H[non_z[0][el], non_z[1][el]] = 0
            H[non_z[1][el], non_z[0][el]] = 0
        mats.append(H)
    mats = np.array(mats)
    return mats