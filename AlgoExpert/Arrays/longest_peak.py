def longestPeakC(array):
    # Write your code here.
    if len(array) < 3:
        return 0
    peak_array = []
    current_array = []
    string = ""
    for i in range(1, len(array)):
        # print("string is {}, index is {}, number is {} and current_array is {} and peak is {}".format(string, i, array[i], current_array, peak_array))
        if array[i] > array[i - 1]:
            if string == "":
                current_array = [array[i - 1], array[i]]
                string = "increasing"
                continue
            if string == "increasing":
                current_array.append(array[i])
                continue
            if string == "decreasing":
                string = "increasing"
                if len(current_array) > len(peak_array):
                    peak_array = current_array
                    current_array = [array[i - 1], array[i]]
        elif array[i] < array[i - 1]:
            if string == "":
                string = "decreasing"
                continue
            if string == "increasing":
                string = "decreasing"
                current_array.append(array[i])
                continue
            if string == "decreasing":
                current_array.append(array[i])
                continue
        elif array[i] == array[i - 1]:
            if string == "increasing":
                current_array = [array[i]]
                continue
            if string == "decreasing":
                string = "increasing"
                if len(current_array) > len(peak_array):
                    peak_array = current_array
                    current_array = [array[i]]

    if len(current_array) > len(peak_array):
        peak_array = current_array

    return peak_array


def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength


print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
print(longestPeak([1, 3, 2]))
print(longestPeak([5, 4, 3, 2, 1, 2, 1]))
