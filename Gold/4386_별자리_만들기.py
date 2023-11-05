import sys
import heapq

n = int(sys.stdin.readline())
stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
stars_dist = [[0] * n for _ in range(n)]


def calculate_dist(x1, x2):
    return round((abs(x2[0] - x1[0]) ** 2 + abs(x2[1] - x1[1]) ** 2) ** 0.5, 2)


def prim(v):
    hq = []
    MST = [0] * n

    heapq.heappush(hq, (0, v))
    sum_dist = 0
    while hq:
        d, v = heapq.heappop(hq)
        if MST[v]:
            continue

        MST[v] = 1
        sum_dist += d

        for i in range(n):
            if not MST[i]:
                heapq.heappush(hq, (stars_dist[v][i], i))
    return sum_dist


for i in range(n):
    for j in range(n):
        stars_dist[i][j] = calculate_dist(stars[i], stars[j])

print(prim(0))
