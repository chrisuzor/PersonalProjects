from functools import reduce

from functools import cached_property
from functools import lru_cache
# Reduce is a function that helps us combine or reduce values in an iterable into one value

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
#
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 6))


class Data:
    def __init__(self, n):
        self.n = n

    @cached_property
    def f(self):
        total = 0
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    total += i + j + k
        return total


# d = Data(200)
# print(d.f)
# print(d.f)
# print(d.f)

@lru_cache
def fib(n):
    print(n)
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))