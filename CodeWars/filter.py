def filter_list(l):

    return [num for num in l if (isinstance(num, int) and num >= 0)]
    # filtered = []
    # for _ in l:
    #     if isinstance(_, int) and _ >= 0:
    #         filtered.append(_)
    # return filtered



print(filter_list([1,2,'aasf','1','123',123]))