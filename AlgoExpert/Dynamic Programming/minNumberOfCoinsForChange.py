def minNumberOfCoinsForChange(n, denoms):
    ways = [float("inf") for _ in range(n + 1)]
    ways[0] = 0
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] = min(ways[amount], 1 + ways[amount - denom])
    print(ways)
    return ways[n] if ways[n] != float("inf") else -1


# print(minNumberOfCoinsForChange(10, [2, 4]))


def numberOfCoinsForChangeB(target, denominations):
    change = [float("inf") for _ in range(0, target + 1)]
    change[0] = 0
    for denomination in denominations:
        for amount in range(1, target + 1):
            if denomination <= amount:
                change[amount] = min(change[amount], 1 + change[amount - denomination])
    print(change)
    return change[target] if change[target] != float("inf") else -1


print(numberOfCoinsForChangeB(7, [1, 5, 10]))
