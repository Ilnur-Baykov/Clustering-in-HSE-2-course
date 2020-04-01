import numpy as np


def remove_from(
        v, G, color, sum_ins,
        sum_out, tot_mas, ver_wei):
    """
    Remove vertex from community
    v - vertex
    G - adjacency matrix
    color - labels color
    sum_ins - sum of edges inside community
    sum_out - sum of edges outside community
    ver_wei - sum of edges, that are connected to vertices
    """

    com_col = color[v]
    k_v = ver_wei[v]
    k_v_in = np.sum(G[v, np.where(color == com_col)])
    sum_ins[com_col] -= k_v_in
    sum_out[com_col] -= (k_v - k_v_in)
    return


def add_to(
        v, to, G, color, sum_ins,
        sum_out, tot_mas, ver_wei):
    """
    Add vertex to community
    v - vertex, that we want to add
    to - vertex, to which community we want to add v
    G - adjacency matrix
    color - labels color
    sum_ins - sum of edges inside community
    sum_out - sum of edges outside community
    tot_mas - sum of all edges
    ver_wei - sum of edges, that are connected to vertices
    """

    com_col = color[to]
    sum_tot = sum_ins[com_col] + sum_out[com_col]
    k_v = ver_wei[v]
    k_v_in = np.sum(G[v, np.where(color == com_col)])
    first = (k_v_in / (2 * tot_mas))
    second = (sum_tot * k_v) / (2 * (tot_mas ** 2))
    add_ans = first - second
    k_v_out = k_v - k_v_in
    return add_ans, k_v_in, k_v_out