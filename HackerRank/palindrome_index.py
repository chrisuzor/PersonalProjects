from collections import defaultdict


def palindromeIndex(s):
    palindrome_dic = {}
    if isPalindrome(s) == "yes":
        return -1
    for i in range(len(s)):
        new_word = s[:i] + s[i + 1 :]

        if new_word not in palindrome_dic:
            palindrome_dic[new_word] = isPalindrome(new_word)
        status = palindrome_dic[new_word]
        print(palindrome_dic)
        if status == "yes":
            return i
    return -1


def isPalindrome(s):
    if s == s[::-1]:
        yield "yes"
    yield "no"


print(palindromeIndex("hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh"))
