def modularity_nx(part, A):
    
    """
    Count of modularity
    part - dictionary of vertex and color
    A - nx.Graph
    """
    
    G = nx.adjacency_matrix(A)
    n = len(part)
    _sum = 0
    m = np.sum(G) / 2
    for i in range(n):
        for j in range(i + 1, n):
            if part[i] == part[j]:
                ki = np.sum(G[i])
                kj = np.sum(G[j])
                _sum += (G[i,j] - ki * kj / (2 * m))
    for i in range(n):
        qwe = np.sum(G[i])
        _sum -= qwe * qwe / (4 * m)
    return _sum / (m)