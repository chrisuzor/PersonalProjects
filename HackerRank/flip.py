def flippingMatrix(matrix):
    # Write your code here
    print("In")
    quadrant = len(matrix) // 2
    for i in range(len(matrix)):
        column = [row[i] for row in matrix]
        lower_bound_column = column[:quadrant]
        uper_bound_column = column[quadrant:]
        if sum(uper_bound_column) > sum(lower_bound_column):
            column = uper_bound_column + lower_bound_column
            for j in range(len(column)):
                matrix[j][i] = column[j]

    for i in range(len(matrix)):
        row = matrix[i]
        lower_bound_row = row[:quadrant]
        uper_bound_row = row[quadrant:]
        if sum(uper_bound_row) > sum(lower_bound_row):
            row = uper_bound_row + lower_bound_row
            matrix[i] = row
    sum_q = 0
    print("Out")
    for i in range(quadrant):
        for j in range(quadrant):
            sum_q += matrix[i][j]
    return sum_q


print(
    flippingMatrix(
        [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    )
)
