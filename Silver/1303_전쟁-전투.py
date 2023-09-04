def bfs(color, a, result):
    queue = [a]
    visited = [a]
    count = 1
    checked[a[0]][a[1]] = 1
    while queue:
        t = queue.pop(0)
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if 0 <= ni < M and 0 <= nj < N \
                    and arr[ni][nj] == color and [ni, nj] not in visited\
                    and not checked[ni][nj]:
                queue.append([ni, nj])
                visited.append(([ni, nj]))
                count += 1
                checked[ni][nj] = 1

    result += count ** 2
    return result


N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
checked = [[0] * N for _ in range(M)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

w_result = b_result = 0
for i in range(M):
    for j in range(N):
        if not checked[i][j]:
            if arr[i][j] == 'W':
                w_result = bfs('W', [i, j], w_result)
            elif arr[i][j] == 'B':
                b_result = bfs('B', [i, j], b_result)

print(w_result, b_result)