k = int(input())
order = input().split()
h = int(input())

row_u = col_l = i = 0
row_d = col_r = 2 ** k - 1

while (row_u != row_d or col_l != col_r) and i < len(order):
    if order[i] == 'R':
        col_l = (col_l + col_r) // 2 + 1
    elif order[i] == 'D':
        row_u = (row_u + row_d) // 2 + 1
    elif order[i] == 'L':
        col_r = (col_l + col_r) // 2
    else:
        row_d = (row_u + row_d) // 2
    i += 1

matrix = [[0] * 2 ** k for _ in range(2 ** k)]

for i in range(2 ** k):
    for j in range(2 ** k):
        if i % 2 == row_u % 2 and j % 2 == col_l % 2:
            matrix[i][j] = h
        elif i % 2 == row_u % 2:
            if h == 1:
                matrix[i][j] = 0
            elif h == 2:
                matrix[i][j] = 3
            elif h == 3:
                matrix[i][j] = 2
            else:
                matrix[i][j] = 1
        elif j % 2 == col_l % 2:
            if h == 1:
                matrix[i][j] = 3
            elif h == 2:
                matrix[i][j] = 0
            elif h == 3:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 2
        else:
            if h == 1:
                matrix[i][j] = 2
            elif h == 2:
                matrix[i][j] = 1
            elif h == 3:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 3

for line in matrix:
    print(*line)