import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(home)

    while q:
        x, y = q.popleft()

        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            print('happy')
            return

        for i in range(n):
            if not visited[i]:
                new_x, new_y = conv[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append(conv[i])
                    visited[i] = True

    print('sad')
    return


for _ in range(int(input())):
    n = int(input())
    home = list(map(int, input().split()))
    conv = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))
    visited = [False] * (n + 2)

    bfs()