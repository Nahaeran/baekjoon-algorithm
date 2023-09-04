import sys
from collections import deque

N = int(sys.stdin.readline())
people = [int(sys.stdin.readline()) for _ in range(N)]

dq = deque()
result = 0

for p in people:
    while dq and dq[-1][0] < p:
        result += dq.pop()[1]

    if not dq:
        dq.append((p, 1))
        continue

    if dq[-1][0] == p:
        cnt = dq.pop()[1]
        result += cnt
        if dq:
            result += 1
        dq.append((p, cnt + 1))
    else:
        dq.append((p, 1))
        result += 1

print(result)