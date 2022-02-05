def sort_array(source_array):
    source_array.sort(key=lambda x: x % 2 == 0)
    print(source_array)

sort_array([5, 3, 2, 8, 1, 4])