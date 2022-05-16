import string

print(string.ascii_uppercase)

uppercase_set = set(string.ascii_uppercase)


def is_upper(s):
    return all(letter in uppercase_set for letter in s)


whitespace_set = set(string.whitespace)


"".join(letter for letter in "HELLO WORLD" if letter not in whitespace_set)


print(all([1, 1, 1, 1]))
