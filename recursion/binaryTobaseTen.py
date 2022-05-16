def findBinary(decimal, result):
    if decimal < 1:
        return result
    result = str((decimal % 2)) + str(result)
    return findBinary(int(decimal / 2), result)


print(findBinary(233, ""))
