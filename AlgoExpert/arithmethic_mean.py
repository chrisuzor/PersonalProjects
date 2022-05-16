def solution(A, S):
    ways = 0
    i = 0
    while i < len(A):
        j = 0
        while j < len(A):
            continous_fragment = A[i : j + 1]
            print(continous_fragment)
            if len(continous_fragment) == 0:
                j += 1
                continue
            arithmetic_mean = sum(continous_fragment) / len(continous_fragment)
            if arithmetic_mean > S:
                j += 1
                continue
            if arithmetic_mean == S:
                print("{} is equal to {}".format(arithmetic_mean, S))
                ways += 1
            j += 1
        i += 1
    return ways


print(solution([2, 1, 3], 2))
# print(solution([0,4,3,-1], 2))
# print(solution([2,1,4], 3))
