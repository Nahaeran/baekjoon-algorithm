import sys

N = int(sys.stdin.readline())
mat_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for term in range(1, N):
    for start in range(N):
        if start + term >= N:
            break

        dp[start][start + term] = int(1e10)

        for i in range(start, start + term):
            dp[start][start + term] = min(dp[start][start + term],
                                          dp[start][i] + dp[i + 1][start + term] + mat_list[start][0] * mat_list[i][1] * mat_list[start + term][1])

print(dp[0][N - 1])
