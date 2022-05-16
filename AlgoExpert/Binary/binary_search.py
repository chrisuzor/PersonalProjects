def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = ((left + right) // 2) - 1
        if array[middle] == target:
            return middle
        if array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


# print(binarySearch([1,3,4,5,6, 7, 8,9,10, 11,12], 9))
print(binarySearch([0, 1, 21, 33, 45, 61, 71, 72, 73], 33))
