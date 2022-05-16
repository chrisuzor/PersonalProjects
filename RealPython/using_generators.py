g = (i for i in range(6))

print(g)

print(next(g))

print(next(g))

# Sum for list
print(sum([i for i in range(1, 10001)]))

# sum for generators
print(sum((i for i in range(1, 10001))))

"""
if you're asked to loop through something , you should use a generator
Also if you need a value one at a time, use a generator
"""


def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd


def main():
    odd_values = [odd for odd in odds(3, 191)]
    print(odd_values)


if __name__ == "__main__":
    main()
