K = int(input())
paths = [[] for _ in range(4)]
directions = [0] * 6
lengths = [0] * 6
for i in range(6):
    d, l = map(int, input().split())
    paths[d - 1].append(l)
    directions[i] = d
    lengths[i] = l

directions *= 2
lengths *= 2
for i in range(6):
    temp = directions[i: i + 2]
    if temp in [[1, 3], [4, 1], [2, 4], [3, 2]]:
        small = lengths[i] * lengths[i + 1]

big = 1
for path in paths:
    if len(path) == 1:
        big *= path[0]
print(K * (big - small))