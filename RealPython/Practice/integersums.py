def add_it_up(number):
    if not isinstance(number, int):
        return 0
    sum_of_integers = 0
    return add_it_up_recursive(number, sum_of_integers)


def add_it_up_recursive(number, sum_of_integers):
    if number == 0:
        return sum_of_integers
    sum_of_integers += number
    number -= 1
    return add_it_up_recursive(number, sum_of_integers)


def even_better(n):
    try:
        result = sum(range(n + 1))
    except TypeError:
        result = 0
    return result


print(add_it_up("b"))
print(add_it_up(4))
