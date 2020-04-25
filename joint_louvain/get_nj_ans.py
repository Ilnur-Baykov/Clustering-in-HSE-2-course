def get_nj_ans(mats, n):
    
    """
    Make not joint clustering
    Returns - answer
    mats - matrices
    n - number of verteces
    """
    
    colors = []
    for i in mats:
        color = np.arange(n)
        data = pre_calc(i, color)
        mid_color = get_new_level(i, color, data[1], data[2], data[0], data[3])
        colors.append(mid_color)
    meta = make_meta_graph(colors)
    meta = np.array(meta)
    meta += meta.T
    color_end = np.arange(n)
    dat = pre_calc(meta, color_end)
    mid_answer = get_new_level(meta, color_end, dat[1], dat[2], dat[0], dat[3])
    return mid_answer