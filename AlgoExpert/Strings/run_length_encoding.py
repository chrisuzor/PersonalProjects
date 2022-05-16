from collections import defaultdict


def runLengthEncodingN(string):
    string_dict = defaultdict(int)
    for s in string:
        string_dict[s] += 1

    final_string = ""
    for key, value in string_dict.items():
        if value > 9:
            times = value // 9
            remainder = value % 9
            final_string += ("9" + key) * times
            final_string += str(remainder) + key
        else:
            final_string += str(value) + key

    return final_string


def runLengthEncoding(string):
    encodedString = []
    currentLength = 1

    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i - 1]

        if currentCharacter != previousCharacter or currentLength == 9:
            encodedString.append(str(currentLength))
            encodedString.append(previousCharacter)
            currentLength = 0
        currentLength += 1

    encodedString.append(str(currentLength))
    encodedString.append(string[len(string) - 1])

    return "".join(encodedString)


# print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
# print(runLengthEncoding("************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"))
print(runLengthEncoding("aAaAaaaaaAaaaAAAABbbbBBBB"))
