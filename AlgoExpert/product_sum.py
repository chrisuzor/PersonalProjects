def productSum(array):
    sum_of_array = 0
    for i in range(0, len(array)):
        if isinstance(array[i], int):
            sum_of_array += array[i]
        else:
            sum_of_array += productSumRecursion(array[i], 2)
    return sum_of_array


def productSumRecursion(array, depth):
    sum_of_array = 0
    for value in array:
        if isinstance(value, list):
            sum_of_array += productSumRecursion(value, depth + 1)
        else:
            sum_of_array += value
    sum_of_array = depth * sum_of_array
    return sum_of_array


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
