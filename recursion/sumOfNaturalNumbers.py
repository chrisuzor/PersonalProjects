def recursiveSummation(number):
    if number <= 1:
        return number
    return number + recursiveSummation(number - 1)

print(recursiveSummation(10))