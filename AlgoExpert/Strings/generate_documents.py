from collections import defaultdict


def generateDocument(characters, document):
    characters_dict = defaultdict(int)
    document_dict = defaultdict(int)
    for ch in characters:
        characters_dict[ch] += 1
    for doc in document:
        document_dict[doc] += 1

    for key, value in document_dict.items():
        document_dict[key] = document_dict[key] - characters_dict[key]

    return all(x <= 0 for x in document_dict.values())


print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))
print(generateDocument("Bste!hetsi ogAxpelrt x ", "AlgoExpert is the Best!"))
