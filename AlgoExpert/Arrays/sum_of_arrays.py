import math


def arrayOfProducts(array):
    product_of_array = math.prod(array)
    final_result = []
    for i in range(len(array)):
        if array[i] == 0:
            first_prod = math.prod(array[0:i])
            second_prod = math.prod(array[i + 1 : len(array)])
            final_result.append(first_prod * second_prod)
        else:
            final_result.append(product_of_array // array[i])
    return final_result


print(arrayOfProducts([5, 1, 4, 2, 0, 6]))
