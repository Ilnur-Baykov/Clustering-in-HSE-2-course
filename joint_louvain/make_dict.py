def make_dict(answer):
    
    """
    Make dictionary form list
    answer - list of colors
    """
    
#     dic = {i: answer[i] for i in range(len(answer))}
    return {i: answer[i] for i in range(len(answer))} #dict(zip(range(len(answer)), answer))