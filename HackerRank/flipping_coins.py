def flipping_coins(coins, amount):
    change_holder = [float("inf") for _ in range(amount + 1)]
    change_holder[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                change_holder[i] = min(change_holder[i], 1 + change_holder[i - coin])
    return change_holder[amount]


print(flipping_coins([100, 50, 25, 10, 5, 1], 126))
