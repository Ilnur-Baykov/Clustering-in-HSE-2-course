def make_joint_list(Matrixes, Colors, count):
    
    """
    Return list that will help to calculate joint clustering
    Matrixes - list of adjacency matrixes
    Colors - list of colors for matrixes
    count - number of matrixes, that we want to add to returning list
    """
    
    mat = []
    for i in range(count):
        hel = []
        hel.append(Matrixes[i])
        tot_mas, sum_ins, sum_out, ver_wei = pre_calc(Matrixes[i], Colors[i])
        hel.append(Colors[i])
        hel.append(tot_mas)
        hel.append(sum_ins)
        hel.append(sum_out)
        hel.append(ver_wei)
        mat.append(hel)
    return mat