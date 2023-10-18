import sys
import heapq


def prim(start):
    heap = []
    MST = [0] * (V + 1)

    heapq.heappush(heap, (0, start))
    sum_weight = 0
    while heap:
        w, v = heapq.heappop(heap)
        if MST[v]:
            continue

        MST[v] = 1
        sum_weight += w

        for next in adj_list[v]:
            if not MST[next[1]]:
                heapq.heappush(heap, (next[0], next[1]))

    return sum_weight


V, E = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    S, E, W = map(int, sys.stdin.readline().split())
    adj_list[S].append((W, E))
    adj_list[E].append((W, S))

print(prim(1))