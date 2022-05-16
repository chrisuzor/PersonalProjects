def reverseWordsInString(string):

    reversed_strings = ""
    start = len(string) - 1
    matched_string = False
    strings_array = []
    for i in range(len(string) - 1, -1, -1):
        reversed_strings += string[i]
        if string[i].isalpha() and matched_string:
            if string[i] == "":
                matched_string = True
            substring = string[i + 1 : start + 1]
            strings_array.append(substring)
            start = i
            reversed_strings = ""

    strings_array.append(reversed_strings[::-1])
    final_result = ""
    print(strings_array)
    for i in range(len(strings_array)):
        final_result += strings_array[i]
    return final_result


print(reverseWordsInString("abc     tuken!"))
