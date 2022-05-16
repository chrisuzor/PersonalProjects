# O(nm*min(n,m)
def longestCommonSubsequence(str1, str2):
    subSequence = [[[] for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                subSequence[i][j] = subSequence[i - 1][j - 1] + [str1[i - 1]]
            else:
                subSequence[i][j] = max(
                    subSequence[i - 1][j], subSequence[i][j - 1], key=len
                )
                # subSequence[i][j] = subSequence[i-1][j] if (len(subSequence[i-1][j])) > (len(subSequence[i][j-1])) else subSequence[i][j-1]
    return subSequence[-1][-1]


def longestCommonSubSequenceBetter(str1, str2):
    lcs = [
        [[None, 0, None, None] for _ in range(len(str1) + 1)]
        for _ in range(len(str2) + 1)
    ]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lcs[i][j] = [str2[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
            else:
                if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]
    return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 and j != 0:
        currentEntry = lcs[i][j]
        if currentEntry[0] is not None:
            sequence.append(currentEntry[0])
        i = currentEntry[2]
        j = currentEntry[3]
    return sequence[::-1]


print(longestCommonSubsequence("zxvvyzw", "xkykzpw"))
print(longestCommonSubSequenceBetter("zxvvyzw", "xkykzpw"))
