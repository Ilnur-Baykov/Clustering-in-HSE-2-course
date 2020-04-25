def make_midle_graph(mats):
    
    """
    Make midle_graph form list of matrices
    Returns matrix - midle graph
    """
    
    n = mats.shape[1]
    ans = np.zeros((n, n))
    for i in mats:
        ans += i
    ans /= len(mats)
    return ans