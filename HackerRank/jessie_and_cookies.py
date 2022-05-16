def cookie(k, A):
    counter = 0
    if len(A) < 2 and A[0] > k:
        return counter

    return cookies_recursive(k, sorted(A), counter)


def cookies_recursive(limit, array, counter):
    print(array)
    if len(array) == 1 and array[0] < limit:
        return -1
    if len(array) < 2:
        return counter
    if array[0] > limit:
        return counter
    smallest = array[0]
    smaller = array[1]
    digit = (1 * smallest) + 2 * smaller
    new_array = array[2:]
    new_array.append(digit)
    counter += 1
    return cookies_recursive(limit, sorted(new_array), counter)


# print(cookie(9, [2,7,3,6,4,6]))
# print(cookie(7, [1,2,3,9,10,12]))
# print(cookie(10, [1,1,1]))
# print(cookie(10, [52, 96, 13, 37]))
print(
    cookie(
        3581,
        [
            6214,
            8543,
            9266,
            1150,
            7498,
            9398,
            1529,
            1032,
            4967,
            1261,
            7384,
            6784,
            34,
            1449,
            7598,
            8795,
            756,
            7803,
            4112,
            298,
            1724,
            4272,
            1100,
            9373,
        ],
    )
)
