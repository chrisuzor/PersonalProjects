def digital_root(n):
    number_to_string = str(n)
    if len(number_to_string) == 1:
        return n
    summation = 0
    for index in range(0, len(number_to_string)):
        summation += int(number_to_string[index])
    return digital_root(summation)


def digital_root_two(n):
    return n if n < 10 else digital_root(sum([int(c) for c in str(n)]))


def digital_root_three(n):
    return n % 9 or n and 9


print(digital_root_three(1321897899))
