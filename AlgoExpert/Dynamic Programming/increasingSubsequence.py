def maxSumIncreasingSubsequence(array):

    if len(array) == 0:
        return 0
    if len(array) == 1:
        return [array[0], array]
    maxSums = array[:]
    maxsum = max(array[0], array[1])
    maxSums[1] = [maxsum, [maxsum]]
    for i in range(2, len(array)):
        remaining_array = array[:i]
        new_sum = array[i]
        subsequence_array = []
        for j in range(0, len(remaining_array)):
            if array[i] > remaining_array[j]:
                subsequence_array.append(remaining_array[j])
                new_sum += remaining_array[j]
        subsequence_array.append(array[i])
        print("{} compared to {}".format(new_sum, maxSums[i - 1][0]))
        if new_sum > maxSums[i - 1][0]:
            print("{} is greater than {}".format(new_sum, maxSums[i - 1][0]))
            maxSums[i] = [new_sum, subsequence_array]
        else:
            print("{} is less than {}".format(new_sum, maxSums[i - 1][0]))
            maxSums[i] = [maxSums[i - 1][0], maxSums[i - 1][1]]

    return maxSums[-1]


def maxSumIncreasingSubsequenceAnswer(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return sequence[::-1]


print(maxSumIncreasingSubsequenceAnswer([8, 12, 2, 3, 15, 5, 7]))
