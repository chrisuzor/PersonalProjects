def findThreeLargestNumbers(array):
    # Write your code here.
    if len(array) <= 3:
        return sorted(array)
    sorted_array = sorted(array[0:3])
    for i in range(3, len(array)):
        if array[i] > sorted_array[0]:
            sorted_array[0] = array[i]
            sorted_array = sorted(sorted_array)
    return sorted_array


print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
