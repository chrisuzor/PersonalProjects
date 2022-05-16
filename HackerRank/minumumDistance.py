def minimumDistances(a):
    # if list(set(a)) == a:
    #     return -1
    min_counter = float("inf")
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                min_counter = min(min_counter, j - i)

    print(min_counter)


# print(minimumDistances([18, 7, 1, 7, 3, 4, 1, 7, 8, 9, 7, 3, 5, 6, 1, 2, 4, 6, 17, 18]))
# print(minimumDistances([ 7, 1, 3, 4, 1, 3, 7, 3]))
print(minimumDistances([7, 1, 3, 7, 1, 2, 3, 2]))
