from collections import defaultdict


def keypad_strings(keys):
    numbers_dict = defaultdict()
    char = 97
    for _ in range(10):
        if _ == 7 or _ == 9:
            key = 4
            numbers_dict[_] = (char, key)
            char += key
        elif _ == 0 or _ == 1:
            numbers_dict[_] = (0, 0)
        else:
            key = 3
            numbers_dict[_] = (char, key)
            char += key
    counter = 0
    result = ""
    for i, key in enumerate(keys):
        if numbers_dict[int(key)][0] == 0:
            continue
        if i > 0 and key == keys[i - 1]:
            counter += 1
        else:
            counter = 0
        char_int = numbers_dict[int(key)][0] + counter
        if counter < numbers_dict[int(key)][1]:
            if counter == 0:
                result += chr(char_int)
            else:
                result = result[:-1] + chr(char_int)
        else:
            counter = 0
            result += chr(char_int)

    return result


# print(keypad_strings('33555336663663'))
print(keypad_strings("111111111"))
print(keypad_strings("22222"))
print(keypad_strings("12345"))
print(keypad_strings("4433555555666"))
