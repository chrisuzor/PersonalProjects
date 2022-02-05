from collections import Counter


def duplicate_count(text):
    counter = Counter(text.upper()).most_common()
    duplicates = 0
    for count in counter:
        if count[1] == 1:
            break
        duplicates += 1
    return duplicates


def duplicate_count_(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)


def duplicate_count__(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

print(duplicate_count("Indivisibilities"))
print(duplicate_count("aA11"))