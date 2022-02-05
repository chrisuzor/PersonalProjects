def binarySearch(array, left, right, x):
    if left > right:
        return -1;
    mid = (left + right) / 2
    if x == array[mid]:
        return mid
    if x < array[mid]:
        binarySearch(array, left, mid - 1, x)
    return binarySearch(array, mid + 1, right, x)