def filter_list(listing):

    return [num for num in listing if (isinstance(num, int) and num >= 0)]


print(filter_list([1, 2, "aasf", "1", "123", 123]))
