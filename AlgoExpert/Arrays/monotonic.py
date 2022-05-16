def isMonotonic(array):
    if len(array) < 3:
        return True
    if array[1] < array[0]:
        monotonic = "decreasing"
    elif array[0] == array[1]:
        monotonic = "equals"
    else:
        monotonic = "increasing"
    for i in range(2, len(array)):
        if monotonic == "equals":
            if array[i] < array[i - 1]:
                monotonic = "decreasing"
            elif array[i] > array[i - 1]:
                monotonic = "increasing"
        if monotonic == "increasing" and array[i] < array[i - 1]:
            return False
        elif monotonic == "decreasing" and array[i] > array[i - 1]:
            return False
    return True


print(isMonotonic([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
