def codeHere(array):
    # Use the function to return the solution.
    maximum_degree = [array[0], 1]
    temp_maximum_degree = [array[0], 1]
    for i in range(1, len(array)):
        if array[i - 1] == array[i]:
            temp_maximum_degree[0] = array[i]
            temp_maximum_degree[1] += 1
            continue
        if maximum_degree[1] < temp_maximum_degree[1]:
            maximum_degree = temp_maximum_degree
            temp_maximum_degree = [array[i], 1]
    if maximum_degree[1] < temp_maximum_degree[1]:
        maximum_degree = temp_maximum_degree
    return maximum_degree[0]


print(codeHere([1, 2, 2, 3, 3, 3, 3, 1, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]))
print(codeHere([1, 2, 2, 1]))
