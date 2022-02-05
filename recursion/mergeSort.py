def mergeSort(array, start, end):
    if start < int(end):
        mid = int((start + end) / 2)
        mergeSort(array, start, mid)
        mergeSort(array, mid + 1, end)
        merge(array, start, mid, end)


def merge(data, start, mid, end):
    temp = list(range(end - start + 1))
    i = start
    j = mid + 1
    k = 0

    while i <= mid and j <= end:
        if data[i] <= data[j]:
            temp[k] = data[i]
            i += 1
            k += 1
        else:
            temp[k] = data[j]
            j += 1
            k += 1

    while i <= mid:
        temp[k] = data[i]
        k += 1
        i += 1

    while j <= end:
        temp[k] = data[j]
        j += 1
        k += 1

    for i in range(start, end + 1):
        data[i] = temp[i - start]


array = [13, 5, 0, -4, 17, 8, 2, 9]
mergeSort(array, 0, 7)
print(array)
