from math import sqrt


def closestStraightCity(c, x, y, q):
    # Write your code here
    cities_coordinates = {}
    for i in range(len(c)):
        shortest_distance = [float("inf"), None]
        for j in range(len(c)):
            if i == j:
                continue
            distance = get_distances(x[i], y[i], x[j], y[j])
            if shortest_distance[0] > distance:
                shortest_distance = [distance, c[j]]
        cities_coordinates[c[i]] = shortest_distance[1]
    string_array = []
    for query in q:
        string_array.append(cities_coordinates[query])

    return string_array


def get_distances(x1, y1, x2, y2):
    if x1 == x2:
        return abs(y1 - y2)
    elif y1 == y2:
        return abs(x1 - y2)
    else:
        return float("inf")


print(
    closestStraightCity(
        ["fastcity", "bigbanana", "xyz"],
        [23, 23, 23],
        [1, 10, 20],
        ["fastcity", "bigbanana", "xyz"],
    )
)
