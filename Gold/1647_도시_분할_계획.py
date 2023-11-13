import sys

N, M = map(int, sys.stdin.readline().split())
edges = [0] * M

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[i] = (a, b, c)

edges.sort(key=lambda x: x[2])

parents = [i for i in range(N + 1)]


def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


cnt = sum_weight = 0
for a, b, c in edges:
    if find_set(a) != find_set(b):
        cnt += 1
        if cnt == N - 1:
            break
        sum_weight += c
        union(a, b)

print(sum_weight)
