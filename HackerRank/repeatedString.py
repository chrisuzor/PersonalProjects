# def repeatedString(s, n):
#     # Write your code here
#     count = 0
#     if len(s) == 1:
#         if s == 'a':
#             return n
#         else:
#             return 0
#     if n > len(s):
#         times = n // len(s)
#         string_append_count = n % len(s)
#         string_to_be_evaluated = s * times
#         string_to_be_evaluated += s[0:string_append_count]
#     else:
#         string_to_be_evaluated = s[:n]
#     for i in range(0, len(string_to_be_evaluated)):
#         if string_to_be_evaluated[i] == 'a':
#             count += 1
#     return count


def repeatedString(s, n):
    count_of_s = len(s)
    if count_of_s == 1:
        if s == "a":
            return n
        else:
            return 0
    count_of_a = 0
    if count_of_s > n:
        remainder_string = s[0:n]
        for j in range(0, len(remainder_string)):
            if s[j] == "a":
                count_of_a += 1
        return count_of_a
    for i in range(0, count_of_s):
        if s[i] == "a":
            count_of_a += 1
    if count_of_s >= n:
        return count_of_a

    duplicate_counts = n // count_of_s
    count_of_a *= duplicate_counts
    remainder_string = s[0 : n % count_of_s]
    for j in range(0, len(remainder_string)):
        if s[j] == "a":
            count_of_a += 1
    return count_of_a


print(repeatedString("aba", 10))
