import string


def caesar(plain_text, shift_num=1):
    letters = string.ascii_lowercase
    print(letters)
    mask = letters[shift_num:] + letters[:shift_num]
    print(mask)
    trantab = str.maketrans(letters, mask)
    print(trantab)
    print(plain_text.translate(trantab))


caesar("abcd xyz", 4)
