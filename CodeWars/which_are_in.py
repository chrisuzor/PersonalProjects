def in_array(array1, array2):
    result = set()
    for word in array1:
        for arr in array2:
            if word in arr:
                result.add(word)
    return sorted(result)


def in_array_(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})


def in_array__(a1, a2):
    return sorted(set(s1 for s1 in a1 if any(s1 in s2 for s2 in a2)))



print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))