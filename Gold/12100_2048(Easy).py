N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0


def game(step, grid, direct):
    global result

    for g in grid:
        result = max(result, max(g))

    if step == 5:
        return

    new_grid = [[0] * N for _ in range(N)]

    if direct == 0:  # 왼
        for i in range(N):
            idx = 0
            tmp = 0
            for j in range(N):
                if grid[i][j]:
                    if tmp == grid[i][j]:
                        new_grid[i][idx] = tmp * 2
                        tmp = 0
                        idx += 1
                    elif tmp != 0:
                        new_grid[i][idx] = tmp
                        tmp = grid[i][j]
                        idx += 1
                    else:
                        tmp = grid[i][j]

            new_grid[i][idx] = tmp

    elif direct == 1:  # 오
        for i in range(N):
            idx = N - 1
            tmp = 0
            for j in range(N - 1, -1, -1):
                if grid[i][j]:
                    if tmp == grid[i][j]:
                        new_grid[i][idx] = tmp * 2
                        tmp = 0
                        idx -= 1
                    elif tmp != 0:
                        new_grid[i][idx] = tmp
                        tmp = grid[i][j]
                        idx -= 1
                    else:
                        tmp = grid[i][j]

            new_grid[i][idx] = tmp

    elif direct == 2:  # 위
        for j in range(N):
            idx = 0
            tmp = 0
            for i in range(N):
                if grid[i][j]:
                    if tmp == grid[i][j]:
                        new_grid[idx][j] = tmp * 2
                        tmp = 0
                        idx += 1
                    elif tmp != 0:
                        new_grid[idx][j] = tmp
                        tmp = grid[i][j]
                        idx += 1
                    else:
                        tmp = grid[i][j]

            new_grid[idx][j] = tmp

    elif direct == 3:  # 아래
        for j in range(N):
            idx = N - 1
            tmp = 0
            for i in range(N - 1, -1, -1):
                if grid[i][j]:
                    if tmp == grid[i][j]:
                        new_grid[idx][j] = tmp * 2
                        tmp = 0
                        idx -= 1
                    elif tmp != 0:
                        new_grid[idx][j] = tmp
                        tmp = grid[i][j]
                        idx -= 1
                    else:
                        tmp = grid[i][j]

            new_grid[idx][j] = tmp

    for i in range(4):
        game(step + 1, new_grid, i)


for i in range(4):
    game(0, board, i)

print(result)