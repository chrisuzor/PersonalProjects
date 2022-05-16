def miniMaxSum(arr):
    # Write your code here
    maximumSum = 0
    minimumSum = sum(arr)
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            summation = sum(arr) - arr[j]
            maximumSum = max(summation, maximumSum)
            minimumSum = min(summation, minimumSum)
    print("{} {}".format(minimumSum, maximumSum))


miniMaxSum([7, 69, 2, 221, 8974])
miniMaxSum([1, 2, 3, 4, 5])
