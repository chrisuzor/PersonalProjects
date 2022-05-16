def nonConstructibleChange(coins):
    coins.sort()
    max_coin_changeable = 0
    for coin in coins:
        if coin > max_coin_changeable + 1:
            return max_coin_changeable + 1
        max_coin_changeable += coin
    return max_coin_changeable + 1
