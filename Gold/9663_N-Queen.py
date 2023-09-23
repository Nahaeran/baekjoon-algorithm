def nqueen(row):
    global result

    if row == N:
        result += 1
        return

    for i in range(N):
        if not visited[i]:
            board[row] = i
            for k in range(row):
                if board[row] == board[k] or abs(board[row] - board[k]) == row - k:
                    break
            else:
                visited[i] = 1
                nqueen(row + 1)
                visited[i] = 0


N = int(input())

board = [0] * N
visited = [0] * N
result = 0

nqueen(0)
print(result)
