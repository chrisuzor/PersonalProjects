def firstNonRepeatingCharacter(string):
    string_dict = {}
    for i in range(len(string)):
        if string[i] in string_dict:
            string_dict[string[i]][1] += 1
        else:
            string_dict[string[i]] = [i, 1]
    for key, value in string_dict.items():
        if value[1] == 1:
            return value[0]
    return -1


print(firstNonRepeatingCharacter("abcdcaf"))
