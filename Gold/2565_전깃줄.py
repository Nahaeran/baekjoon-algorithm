import sys

N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lines.sort(key=lambda x: x[0])
LIS = [lines[0]]


def binary_search(target):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2
        if LIS[mid][1] == target:
            return mid
        elif LIS[mid][1] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start


for line in lines:
    if LIS[-1][1] < line[1]:
        LIS.append(line)
    else:
        idx = binary_search(line[1])
        LIS[idx] = line

print(N - len(LIS))
