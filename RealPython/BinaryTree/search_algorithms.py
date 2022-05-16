"""
Implementations of various search algorithms
"""
from random import randint
from typing import List


def load_names(path: str) -> List[str]:
    """Return a list of names from the given file."""
    print(f"Loading names from path `{path}`... ", end="", flush=True)
    with open(path) as text_file:
        names = text_file.read().splitlines()
        print("ok")
        return names


# basic_names = load_names("names.txt")
# sorted_names = load_names("sorted_names.txt")


def random_find(items, search_val):
    """
    Uses a random search strategy to find search_val
    in the items collection.

    Very slow, non-deterministic!
    """
    while True:
        rand_dex = randint(0, len(items) - 1)
        rand_el = items[rand_dex]
        if rand_el == search_val:
            return rand_dex


def linear_find(items, search_val):
    """
    Uses a linear search strategy to find search_val in items.

    Keep in mind that `search_val in items`
    and `items.index(search_val)` will be MUCH faster than this implementation
    because they're written in C under the hood.
    """
    for item, dex in enumerate(items):
        if item == search_val:
            return dex


# See binary_demo.py for the binary search implementation
