from collections import Counter, defaultdict


def top_three_letters(string):
    counter = defaultdict(int)
    for c in string:
        counter[c] += 1
    top_three = sorted(counter, key=lambda k: counter[k], reverse=True)[:3]
    result = []
    for letter in top_three:
        result.append((letter, counter[letter]))
    print(result)


def top_three_letters_best(string):
    return Counter(string).most_common(3)


top_three_letters(
    "kfnkfdnlndfknfdknkfdanjknakjnjknkdfnkjnsdfnjbnjdsfbnjbjsbkbsjbkjbeijbaibajbakfdka"
)
print(
    top_three_letters_best(
        "kfnkfdnlndfknfdknkfdanjknakjnjknkdfnkjnsdfnjbnjdsfbnjbjsbkbsjbkjbeijbaibajbakfdka"
    )
)
