import re


def solution(T, R):
    nathan_scores = {}

    for i in range(len(T)):
        tests = T[i]
        result = R[i]
        match = re.match(r"([a-z]+)([0-9]+)", tests, re.I)
        if match:
            items = match.groups()
            test_group = items[0] + items[1]
            if test_group in nathan_scores:
                if result != "OK":
                    nathan_scores[test_group] = False
            else:
                if result == "OK":
                    nathan_scores[test_group] = True
                else:
                    nathan_scores[test_group] = False
    print(nathan_scores)
    scores = 0
    for item in nathan_scores:
        if nathan_scores[item] == True:
            scores += 1
    return round(scores * 100 / len(nathan_scores))


test3 = [
    "test1",
    "test2a",
    "test2b",
    "test4",
    "test2c",
    "test3",
    "test5",
    "test6",
    "test7",
]
results3 = [
    "OK",
    "OK",
    "TimeOut",
    "OK",
    "TimeOut",
    "OK",
    "TimeOut",
    "Runtime " "error",
    "OK",
]

print(solution(test3, results3))
