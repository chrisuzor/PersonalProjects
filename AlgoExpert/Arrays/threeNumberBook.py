def threeNumberSum(array, targetSum):
    array_target = []
    if len(array) < 3:
        return array_target
    for i in range(0, len(array) - 2):
        for j in range(1, len(array)):
            for k in range(2, len(array)):
                if i == k:
                    continue
                if i == j:
                    continue
                if k == j:
                    continue
                target_sum_array = [array[i], array[j], array[k]]
                if targetSum == sum(target_sum_array):
                    if sorted(target_sum_array) not in array_target:
                        array_target.append(sorted(target_sum_array))

    return sorted(array_target)


def threeNumbersSumBetter(array, target):
    array.sort()
    triplets = []
    for i in range(0, len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            target_array = [array[i], array[left], array[right]]
            if sum(target_array) == target:
                triplets.append(target_array)
                left += 1
                right -= 1
            elif sum(target_array) < target:
                left += 1
            elif sum(target_array) > target:
                right -= 1
    return triplets


# print(threeNumberSum([2,3,7,8,1,9,11,34], 18))
# print(threeNumberSum([12,3,1,2,-6,5,-8,6], 0))
# print(threeNumberSum([1,2,3], 7))
# print(threeNumberSum([8,10,-2,49,14], 57))
print(threeNumbersSumBetter([12, 3, 1, 2, -6, 5, 0, -8, -1], 0))
