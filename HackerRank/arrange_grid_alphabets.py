def gridChallenge(grid):
    if len(grid) == 0:
        return "NO"
    print(len(grid[0]))
    print(len(grid))
    for i in range(len(grid)):
        row = sorted(grid[i])
        # print(row)
        grid[i] = row
    # print('---------------------------------')
    possible = "Yes"
    for i in range(len(grid[0])):
        column = [row[i] for row in grid]
        # print(column)
        if column != sorted(column):
            possible = "No"
        # print('+++++++++++++++++++++++++++++++')
        # print(column)
        # for j in range(len(column)):
        #     grid[j][i] = column[j]

    print(grid)
    print(possible)


# gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])
gridChallenge(["abc", "hjk", "mpq", "rtv"])
