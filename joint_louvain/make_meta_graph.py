def make_meta_graph(colors):
    
    """
    Make meta_graph form list of colors
    Returns matrix - meta graph (not symmetric)
    """
    
    colors = np.array(colors)
    n = colors.shape[1]
    row, col = np.triu_indices(n, k=1)
    meta_graph = np.zeros((n,n))
    for i,j in zip(row, col):
        meta_graph[i, j] = np.mean(colors[:, i] == colors[:, j])
        meta_graph[i, j] = meta_graph[i, j]
    return meta_graph