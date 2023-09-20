import sys

N = int(input())
power = []
for _ in range(N):
    power.append(list(map(int, sys.stdin.readline().split())))
state = list(input())
state = state[::-1]

bit, count = 0, 0
for s in state:
    bit <<= 1
    if s == 'Y':
        bit |= 1
        count += 1
P = int(input())

dp = [float('inf') for _ in range(1 << N)]


def DFS(s, cnt):
    if cnt >= P:
        return 0

    if dp[s] != float('inf'):
        return dp[s]

    min_cost = float('inf')
    for i in range(N):
        if s & (1 << i):
            for j in range(N):
                if s & (1 << j) == 0:
                    cost = power[i][j] + DFS(s | 1 << j, cnt + 1)
                    min_cost = min(cost, min_cost)
                dp[s] = min_cost

    return min_cost


result = DFS(bit, count)
print(-1 if result == float('inf') else result)