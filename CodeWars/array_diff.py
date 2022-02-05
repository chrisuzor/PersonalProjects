def array_diff(a, b):
    set_a = set(a)
    set_b = set(b)
    for _ in set_b:
        if _ in set_a:
            a = list(filter(_.__ne__, a))

    return a


def array_diff_two(a, b):
    return [x for x in a if x not in set(b)]


print(array_diff([1, 2, 2, 2, 3], [2]))
