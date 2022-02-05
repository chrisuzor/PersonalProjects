# Generally you should use sets when you need to filter through duplicates

def count_unique_list(string):
    seen_c = []
    for c in string:
        if c not in seen_c:
            seen_c.append(c)
    return len(seen_c)


def count_unique_set(string):
    seen_c = set()
    for c in string:
        if c not in seen_c:
            seen_c.add(c)
    return len(seen_c)


def count_unique_set_comprehension(string):
    return len({c for c in string})


def count_unique_sage_mode(string):
    return len(set(string))


print(count_unique_list('jhdfbhjbvhsvhvbsjdvhrvyveryervjchmnxbsjhdfbfdviudbbi'))
print(count_unique_set('jhdfbhjbvhsvhvbsjdvhrvyveryervjchmnxbsjhdfbfdviudbbi'))
print(count_unique_set_comprehension('jhdfbhjbvhsvhvbsjdvhrvyveryervjchmnxbsjhdfbfdviudbbi'))