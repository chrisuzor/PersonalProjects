def isPalindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word[len(word) - 1]:
        return isPalindrome(word[1:len(word)-1])
    return False

print(isPalindrome("level"))
print(isPalindrome("levela"))
print(isPalindrome("jewel"))
print(isPalindrome("racecar"))