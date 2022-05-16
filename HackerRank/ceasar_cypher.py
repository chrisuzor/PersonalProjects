import string

A = 65
Z = 90
a = 97
z = 122


def ceaserCipher(s, k):
    new = ""
    k = k % 26
    for word in s:
        if word.isalpha():
            number_numeric = ord(word) + k
            if word.isupper():
                if number_numeric > ord("Z"):
                    difference = number_numeric - ord("Z")
                    number_numeric = ord("A") + difference - 1
            elif word.islower():
                if number_numeric > ord("z"):
                    difference = number_numeric - ord("z")
                    number_numeric = ord("a") + difference - 1
                    print(number_numeric)
            word = chr(number_numeric)
        new += word
    return new


# print(2 % 26)

print(ceaserCipher("www.abc.xy", 87))
