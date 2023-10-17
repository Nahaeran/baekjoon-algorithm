import sys
sys.setrecursionlimit(10**7)

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

N = int(input())

forest = [list(map(int, input().split())) for _ in range(N)]
result = 1
dp = [[-1] * N for _ in range(N)]


def dfs(x, y):
    global result
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 1

    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < N and forest[x][y] < forest[ni][nj]:
            dp[x][y] = max(dp[x][y], dfs(ni, nj) + 1)
    return dp[x][y]


for i in range(N):
    for j in range(N):
        result = max(result, dfs(i, j))

print(result)
