def firstDuplicateValue(array):
    counter = {}
    for value in array:
        if value in counter:
            return value
        else:
            counter[value] = 1

    return -1
