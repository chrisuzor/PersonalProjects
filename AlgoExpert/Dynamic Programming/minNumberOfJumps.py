def minNumberOfJumps(array):
    if len(array) == 0 or 1:
        return len(array)

    steps = [float("inf") for _ in range(0, len(array))]
    steps[0] = 0
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] >= i - j:
                steps[i] = min(steps[j] + 1, steps[i])
    return steps[-1]


def minNumberOfJumpsBetter(array):
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1


print(minNumberOfJumps([3, 4, 2, 1, 1, 3, 7, 1, 1, 1, 3]))
