from collections import defaultdict


def findSequence(array):
    word_counter = defaultdict(int)
    words_sequence = {}
    for word in array:
        words = word.split(">")
        word_counter[words[0]] += 1
        word_counter[words[1]] += 2
        words_sequence[words[0]] = words[1]

    string = ""
    for key, value in word_counter.items():
        if value == 1:
            string += key
            break
    return findSequenceRecursive(string, array, words_sequence)


def findSequenceRecursive(string, arr, word_dict):
    if len(string) == len(arr) + 1:
        return string
    word = string[-1]
    next_word = word_dict[word]
    string += next_word
    return findSequenceRecursive(string, arr, word_dict)


print(findSequence(["P>A", "I>N", "A>I", "S>P"]))
print(findSequence(["P>E", "E>R", "R>U"]))
print(findSequence(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]))
