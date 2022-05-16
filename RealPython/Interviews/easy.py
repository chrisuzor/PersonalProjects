from collections import Counter


def majority_element_indexes(lst):
    majority_element = len(lst) // 2
    cnt = Counter(lst)
    return [
        index for index, element in enumerate(lst) if cnt[element] > majority_element
    ]
