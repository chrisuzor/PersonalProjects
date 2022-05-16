def moveElementToEnd(array, toMove):
    numbers_to_move = 0
    for i in range(len(array)):
        if array[i] == toMove:
            numbers_to_move += 1
        else:
            if numbers_to_move > 0:
                array[i - numbers_to_move], array[i] = array[i], toMove
    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
