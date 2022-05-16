def twoNumberSum(array, targetSum):
    left = 0
    right = len(array) - 1
    array.sort()
    while left < right:
        two_number_sum = array[left] + array[right]
        if two_number_sum == targetSum:
            return [array[left], array[right]]
        elif targetSum > two_number_sum:
            left += 1
        else:
            right -= 1
    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
