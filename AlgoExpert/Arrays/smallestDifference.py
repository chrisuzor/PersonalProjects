def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    abs_array = [arrayOne[0], arrayTwo[0], abs(arrayOne[0] - arrayTwo[0])]
    i = 0
    print(abs_array)
    while i < len(arrayOne):
        for j in range(len(arrayTwo)):
            print("J is {} and value is {}".format(j, arrayTwo[j]))
            if abs_array[2] > abs(arrayOne[i] - arrayTwo[j]):
                print("Previous ABS ARRAY is {}".format(abs_array))
                abs_array = [arrayOne[i], arrayTwo[j], abs(arrayOne[i] - arrayTwo[j])]
                print("Updated ABS ARRAY is {}".format(abs_array))
        i += 1

    return abs_array[0:2]


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
