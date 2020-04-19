def modularity(part, G):
    
    """
    Count of modularity
    part - dictionary of vertex and color
    A - np.array
    """
    
    n = len(G[0])
    degrees = G.sum(axis=1)
    _sum = 0
    m = np.sum(G) / 2
    for i in range(n):
        for j in range(i + 1, n):
            if i == j:
                _sum -= ki * kj / m
            if part[i] == part[j]:
                ki = degrees[i]
                kj = degrees[j]
                _sum += (G[i][j] - ki * kj / (2 * m))
    for i in range(n):
        qwe = degrees[i]
        _sum -= qwe * qwe / (4 * m)
    return _sum / m