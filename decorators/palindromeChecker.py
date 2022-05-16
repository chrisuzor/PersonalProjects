import math as ma


def change(input):
    length = len(input)

    # counts the number of differences
    # which prevents the string from
    # being palindrome.
    diffCount = 0
    i = 0

    # keeps a record of the characters
    # that prevents the string from
    # being palindrome.
    diff = [["0"] * 2] * length
    # loops from the start of a string
    # till the midpoint of the string
    while i < length // 2:

        # difference is encountered preventing
        # the string from being palindrome
        if input[i] != input[length - i - 1]:

            # 3rd differences encountered and
            # its no longer possible to make
            # is palindrome by one swap
            # if diffCount == 2:
            #     return False

            # record the different character
            diff[diffCount][0] = input[i]

            # store the different characters
            diff[diffCount][1] = input[length - i - 1]
            diffCount += 1
        i += 1
    print(diff)
    return diffCount


def isPalindrome(s):
    return s == s[::-1]


def palindromeChecker(s, startIndex, endIndex, subs):
    result = ""
    len_of_checks = len(startIndex)
    for i in range(0, len_of_checks):
        start = startIndex[i]

        end = endIndex[i]
        sub = subs[i]
        new_string = s[start : end + 1]
        print("-----------")
        print(sub)
        print(new_string)
        print(change(new_string))
        print(isPalindrome(new_string))
        if isPalindrome(new_string) or sub >= change(new_string):
            result += "1"
        else:
            result += "0"
        print(result)


palindromeChecker("cdecd", [0, 0, 0, 0], [0, 1, 2, 3], [0, 1, 1, 0])
palindromeChecker("xxdnssuqevu", [0], [10], [3])

# print(change('xxdnssuqevu'))
print(change("cdecd"))
# print(change('level'))


def subsegmentSort(arr):
    N = len(arr)

    # To keep track of max
    # and min elements at every index
    leftMax = []
    rightMin = []

    leftMax.append(arr[0])

    for i in range(1, N):
        leftMax.append(max(leftMax[i - 1], arr[i]))

    rightMin.append(arr[N - 1])

    for i in range(1, N):
        rightMin.append(min(rightMin[i - 1], arr[N - i - 1]))
    rightMin.reverse()
    count = 0

    for i in range(0, N - 1):
        if leftMax[i] <= rightMin[i + 1]:
            count = count + 1

    # Return count + 1 as the final answer
    return count + 1


arr = [10, 0, 21, 32, 68]
# print(subsegmentSort(arr))
