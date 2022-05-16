def selectionSort(array):
    currendIdx = 0
    while currendIdx < len(array) - 1:
        smallestIdx = currendIdx
        for i in range(currendIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
            array[currendIdx], array[smallestIdx] = (
                array[smallestIdx],
                array[currendIdx],
            )
            currendIdx += 1
    return array
