def solve(m, s):
    two_dimensional_array = []
    multiplier_array = []
    for word in s:
        two_dimensional_array.append(list(map(lambda letter: ord(letter), word)))
    print(two_dimensional_array)
    sum_of_a = 0
    for array in two_dimensional_array:
        print(sum(array))
        sum_of_a += sum(array)
        multiplier_array.append(next(multiply_recursion(array, m)))
    print(sum_of_a ** m)
    return "EVEN" if sum(multiplier_array) % 2 == 0 else "ODD"


def multiply_recursion(array, m):
    current_multiplier = 1
    for value in array:
        current_value = value ** m
        current_multiplier *= current_value
    yield current_multiplier


print(solve(2, ["azbde", "abcher", "acegk"]))
