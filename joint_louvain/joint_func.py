def joint_func(index_sum, modul_sum):
    
    """
    Function that returns vertex based on index_sum and modul_sum information
    index_sum - index_sum
    modul_sum - modul_sum
    """
    
    ind = np.nonzero(index_sum)[0]
    if len(ind) == 0:
        return -1
    for j in ind:
        modul_sum[j] /= index_sum[j]
    result = np.where(modul_sum == np.amax(modul_sum))
    idi = random.randint(0, len(result[0]) - 1)
    return result[0][idi]