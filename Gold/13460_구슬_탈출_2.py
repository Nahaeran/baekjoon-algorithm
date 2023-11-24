import sys
from collections import deque

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(N)]
visited = set()

result = 0


def bfs(r, b):
    q = deque([(r, b, 0)])
    visited.add((r[0], r[1], b[0], b[1]))

    while q:
        r, b, count = q.popleft()
        if count > 10:
            continue
        if board[r[0]][r[1]] == 'O':
            return count

        for k in range(4):
            r_count = b_count = 0

            ni_r = r[0]
            nj_r = r[1]
            ni_b = b[0]
            nj_b = b[1]

            while True:
                ni_r += di[k]
                nj_r += dj[k]
                if board[ni_r][nj_r] == '#':
                    ni_r -= di[k]
                    nj_r -= dj[k]
                    break
                if board[ni_r][nj_r] == 'O':
                    break
                r_count += 1

            while True:
                ni_b += di[k]
                nj_b += dj[k]
                if board[ni_b][nj_b] == '#':
                    ni_b -= di[k]
                    nj_b -= dj[k]
                    break
                if board[ni_b][nj_b] == 'O':
                    break
                b_count += 1

            if board[ni_b][nj_b] == 'O':
                continue

            # 두 구슬의 위치가 똑같을 때
            if ni_r == ni_b and nj_r == nj_b:
                if r_count > b_count:
                    ni_r -= di[k]
                    nj_r -= dj[k]
                else:
                    ni_b -= di[k]
                    nj_b -= dj[k]

            if (ni_r, nj_r, ni_b, nj_b) not in visited:
                q.append(((ni_r, nj_r), (ni_b, nj_b), count + 1))
                visited.add((ni_r, nj_r, ni_b, nj_b))
    return -1


for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            ri = i
            rj = j
        if board[i][j] == 'B':
            bi = i
            bj = j

print(bfs((ri, rj), (bi, bj)))
