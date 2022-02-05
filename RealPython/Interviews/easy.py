from collections import Counter


def majority_element_indexes(lst):
    majority_element = len(lst) // 2
    cnt = Counter(lst)
    return [index for index, element in enumerate(lst) if cnt[element] > majority_element]


print(majority_element_indexes([1, 2, 3, 4, 1, 1, 4, 4, 5, 1, 4, 2, 5, 1, 1, 1, 1, 1, 1]))