def binary_tree_search(elements, item):
    # set lower and upper boundary
    lower, upper = 0, len(elements) - 1
    while lower <= upper:
        # middle_index = (lower + upper) // 2
        # because of integer overflow, best to use the below
        middle_index = lower + (upper - lower) // 2
        middle_element = elements[middle_index]

        if middle_element == item:
            return middle_index
        if middle_element < item:
            lower = middle_index + 1
        else:
            upper = middle_index - 1

    return None


elements = [2, 3, 4, 5, 6, 8, 9, 11, 14, 17, 18]
print(binary_tree_search(elements, 9))
