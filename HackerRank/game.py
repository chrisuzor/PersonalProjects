def getMinimalCost(parcel, number):
    parcel.sort()
    remaining_parcel = []
    remaining_parcel_no = number - len(parcel)
    counter = number - len(parcel)
    lowest = 1
    i = 0
    if remaining_parcel_no > 0:
        while remaining_parcel_no <= number and len(remaining_parcel) < counter:
            if i < len(parcel):
                if parcel[i] == lowest:
                    lowest += 1
                    i += 1
                    continue

            remaining_parcel.append(lowest)
            lowest += 1
            remaining_parcel_no += 1
    return sum(remaining_parcel)


def printMissingElements(arr, N):
    # Initialize diff
    diff = arr[0]

    for i in range(N):

        # Check if diff and arr[i]-i
        # both are equal or not
        if arr[i] - i != diff:

            # Loop for consecutive
            # missing elements
            while diff < arr[i] - i:
                print(i + diff, end=" ")
                diff += 1


print(getMinimalCost([2, 3, 6, 8, 10], 9))
print(getMinimalCost([6, 5, 4, 1, 3], 7))
print(getMinimalCost([4, 5, 7, 1], 4))
