def reverseString(word):
    if word == "":
        return ""
    return reverseString(word[1:]) + word[0]


print(reverseString("hello"))
