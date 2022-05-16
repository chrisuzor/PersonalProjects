def smallestWay(num):
    memoization_array = [num + 1 for _ in range(0, num + 1)]
    memoization_array[0] = 0
    memoization_array[1] = 1
    memoization_array[2] = 1
    memoization_array[3] = 1
    for i in range(4, num + 1):
        if num >= i:
            if i % 3 == 0 and i % 2 == 0:
                memoization_array[i] = 1 + min(
                    memoization_array[i // 3],
                    memoization_array[i // 2],
                    memoization_array[i - 1],
                )
            else:
                if i % 3 == 0:
                    memoization_array[i] = 1 + min(
                        memoization_array[i // 3], memoization_array[i - 1]
                    )
                elif i % 2 == 0:
                    memoization_array[i] = 1 + min(
                        memoization_array[i // 2], memoization_array[i - 1]
                    )
                else:
                    memoization_array[i] = 1 + memoization_array[i - 1]
        print("{} is {}".format(i, memoization_array[i]))

    return memoization_array[num]


print(smallestWay(11))
