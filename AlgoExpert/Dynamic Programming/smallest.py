# This is a demo task.
#
# Write a function:
#
#     def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].


def solution(A):
    A = sorted(list(set(A)))
    smallest = A[-1] + 1
    for i in range(1, len(A)):
        if A[i - 1] + 1 < A[i]:
            smallest = min(smallest, A[i - 1] + 1)
    return smallest if smallest > 0 else 1


# print(solution([1, 3, 6, 4, 1, 2]))
# print(solution([1, 2, 3]))
# print(solution([-1, -3]))
# print(solution([1,2,3,5,6,7,7,88,9,0,0,2,3,4,5,66,]))


def solutionB(N):
    # write your code in Python 3.6
    binary = "{0:b}".format(N)
    max_value = 0
    counter = 0
    print(binary)
    for i in range(1, len(binary)):
        if binary[i] == "0":
            counter += 1
        else:
            max_value = max(counter, max_value)
            counter = 0
    return max_value


# print(solutionB(20))
# print(solutionB(9))
# print(solutionB(529))


def solutionInverse(arr):
    inv_count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count


# print(solutionInverse([-1, 6, 3, 4, 7, 5]))
print(solutionInverse([5, 4, 3, 2, 1]))
