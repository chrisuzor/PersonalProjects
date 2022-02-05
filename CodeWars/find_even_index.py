def find_even_index(arr):
    for index in range(0, len(arr)):
        if sum(arr[:index]) == sum(arr[index + 1:]):
            return index
    return -1


print(find_even_index([20,10,-80,10,10,15,35]))

print(find_even_index([1,2,3,4,5,6]))

print(find_even_index([0,0,0,0,0]))

print(find_even_index(list(range(-100,-1))))

