import sys
import heapq

input = sys.stdin.readline

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
tc = 1

while True:
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    distance = [[int(1000000000) for _ in range(N)] for _ in range(N)]

    heap = []
    heapq.heappush(heap, (cave[0][0], 0, 0))

    while heap:
        dist, x, y = heapq.heappop(heap)
        if distance[x][y] < dist:
            continue
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < N and 0 <= ny < N and cave[nx][ny] + dist < distance[nx][ny]:
                distance[nx][ny] = cave[nx][ny] + dist
                heapq.heappush(heap, (distance[nx][ny], nx, ny))

    print(f"Problem {tc}: {distance[N - 1][N - 1]}")
    tc += 1
