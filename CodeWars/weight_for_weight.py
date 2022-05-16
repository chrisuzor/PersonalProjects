def order_weight(strings):
    get_weight_tuples = [
        sum_digit_together(string) for string in sorted(strings.split())
    ]
    get_weight_tuples.sort(key=lambda x: x[1])
    weight_strings = [get_weight_tuple[0] for get_weight_tuple in get_weight_tuples]
    return " ".join(weight_strings)


def sum_digit_together(digit_string):
    return digit_string, sum(list(map(int, digit_string)))


def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum


def order_weight_one(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))
    return result


def order_weight_two(_str):
    return " ".join(
        sorted(sorted(_str.split(" ")), key=lambda x: sum(int(c) for c in x))
    )


print(order_weight("103 123 4444 99 2000"))
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
print(order_weight(""))
