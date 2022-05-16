def max_earnings(earnings_per_fight):
    num_fights = len(earnings_per_fight)
    if num_fights == 0:
        return 0
    if num_fights == 1:
        return 0

    earning_array = [earnings_per_fight[0]]

    i = 2
    while i <= num_fights:
        try:
            earning_array.append(max(earnings_per_fight[i], earnings_per_fight[i - 1]))
        except IndexError:
            if i == num_fights:
                earning_array.append(earnings_per_fight[i - 1])
            else:
                earning_array.append(earnings_per_fight[i])
        i += 2

    return sum(earning_array)


print(max_earnings([1, 2, 5, 2, 3]))
print(max_earnings([6, 2, 95, 94]))
