def create_phone_number(n):
    phone_number_string = ''
    i = 0
    for _ in n:
        if i == 0:
            phone_number_string += '('
        if i == 3:
            phone_number_string += ') '
        if i == 6:
            phone_number_string += '-'
        phone_number_string += str(_)
        i += 1
    return phone_number_string


def create_phone_number_two(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number_three(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"


def create_phone_number_four(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
