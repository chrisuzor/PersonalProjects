from functools import lru_cache


def getNthFib(n):
    if n == 0:
        return 0
    n -= 1
    return getNthFibRecursive(n)


@lru_cache()
def getNthFibRecursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return getNthFibRecursive(n - 1) + getNthFibRecursive(n - 2)


print(getNthFib(6))
