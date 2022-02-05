import math

def square_numbers(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]

squared = map(square_numbers, numbers)

print(list(map(lambda x: x ** 2, numbers)))


def rotate_chr(c):

    rot_by = 3

    c = c.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Keep punctuation and whitespace

    if c not in alphabet:

        return c

    rotated_pos = ord(c) + rot_by

    # If the rotation is inside the alphabet

    if rotated_pos <= ord(alphabet[-1]):

        return chr(rotated_pos)

    # If the rotation goes beyond the alphabet

    return chr(rotated_pos - len(alphabet))


print("".join(map(rotate_chr, "My secret message goes here.")))


def is_positive(num):
    return num >= 0


def sanitized_sqrt(numbers_):
    return list(map(math.sqrt, filter(is_positive, numbers_)))


print(sanitized_sqrt([25, 9, 81, -16, 0]))


list(map(square_numbers, numbers))

# list comprehension
[square_numbers(x) for x in numbers]

# generator expression
list(square_numbers(x) for x in numbers)
