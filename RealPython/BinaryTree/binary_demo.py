# binary_demo.py


def binary_iterative(elements, search_item):
    """
    Return the index of the search_item, or None if not found.
    No guarantees as to *which* index of the search item is returned,
    if multiple exist.
    """

    left, right = 0, len(elements) - 1

    while left <= right:

        middle_dex = (left + right) // 2
        middle_el = elements[middle_dex]

        if middle_el == search_item:
            return middle_dex
        elif middle_el < search_item:
            left = middle_dex + 1
        elif middle_el > search_item:
            right = middle_dex - 1

    return None


def binary_recursive(elements, search_item, dex_mod=0):
    """
    Return the index of the search_item, or None if not found.
    No guarantees as to *which* index of the search item is returned,
    if multiple exist.

    Recursive implementation
    """

    while elements:

        middle_dex = len(elements) // 2
        middle_el = elements[middle_dex]

        if middle_el == search_item:
            return middle_dex + dex_mod
        elif middle_el < search_item:
            # Need to modify dex_mod on this call because you're discarding
            # elements from the left side of the list.
            return binary_recursive(
                elements[middle_dex + 1 :], search_item, dex_mod + middle_dex + 1
            )
        elif middle_el > search_item:
            return binary_recursive(elements[:middle_dex], search_item, dex_mod)

    return None


def binary_leftmost(elements, search_item):
    """
    Uses binary search to find the leftmost index of a given element.

    Careful, this algorithm can be O(n) in the rare worst case
    (which is when all elements are the search element)
    If you want to ensure this algorithm is O(log(n)),
    try modifying the binary_iterative function itself.
    """
    tentative = binary_iterative(elements, search_item)
    if tentative is None:
        return None
    while elements[tentative] == search_item and tentative >= 0:
        tentative -= 1
    return tentative + 1
