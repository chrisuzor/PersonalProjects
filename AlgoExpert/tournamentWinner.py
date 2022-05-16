from collections import defaultdict


def tournamentWinner(competitions, results):
    result_counter = defaultdict(int)
    for i in range(0, len(competitions)):
        teams = competitions[i]
        result = results[i]
        if result == 1:
            result_counter[teams[0]] += 1
        else:
            result_counter[teams[1]] += 1

    return max(result_counter, key=lambda k: result_counter[k])


print(
    tournamentWinner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1])
)
