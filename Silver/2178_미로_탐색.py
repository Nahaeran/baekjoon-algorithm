import sys
from collections import deque

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

q = deque([(0, 0, 1)])

while q:
    i, j, count = q.popleft()

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == '1':
            board[ni][nj] = '0'
            if ni == N - 1 and nj == M - 1:
                print(count + 1)
                q.clear()
                break
            q.append((ni, nj, count + 1))
