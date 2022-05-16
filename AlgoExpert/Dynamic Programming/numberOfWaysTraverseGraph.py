# Time O(2^(n + m)) | Space O(n + m)
def numberOfWaysToTraverseGraphRecursion(width, height):
    if width == 1 or height == 1:
        return 1
    return numberOfWaysToTraverseGraphRecursion(
        width - 1, height
    ) + numberOfWaysToTraverseGraphRecursion(width, height - 1)


# Time O(nm) | Space O(nm)
def numberOfWaysToTraverseGraphDynamicProgramming(width, height):
    numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for widthPosition in range(1, width + 1):
        for heightPosition in range(1, height + 1):
            if widthPosition == 1 or heightPosition == 1:
                numberOfWays[heightPosition][widthPosition] = 1
            else:
                waysLeft = numberOfWays[heightPosition][widthPosition - 1]
                waysUp = numberOfWays[heightPosition - 1][widthPosition]
                numberOfWays[heightPosition][widthPosition] = waysUp + waysLeft

    return numberOfWays[height][width]


# Time O(n + m) | Space O(1)
def numberOfWaysToTraverseGraphmaths(width, height):
    distanceToRight = width - 1
    distanceToBottom = height - 1
    numerator = factorial(distanceToRight + distanceToBottom)
    denominator = factorial(distanceToRight) * factorial(distanceToBottom)
    return numerator // denominator


def factorial(num):
    result = 1

    for n in range(2, num + 1):
        result *= n

    return result


print(numberOfWaysToTraverseGraphRecursion(2, 3))
print(numberOfWaysToTraverseGraphDynamicProgramming(2, 3))
print(numberOfWaysToTraverseGraphmaths(2, 3))
