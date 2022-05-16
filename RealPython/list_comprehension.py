num_rows = 2
num_columns = 3
grid = []

for _ in range(num_rows):
    current_row = []
    for _ in range(num_columns):
        current_row.append(0)
    grid.append(current_row)

grid = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

print(grid)
