import sys

N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lines.sort(key=lambda x: x[0])
lines_a = list(map(lambda x: x[0], lines))

LIS = [lines[0]]
dp = [(0, lines[0][0])]


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
        dp.append((len(LIS) - 1, line[0]))
    else:
        idx = binary_search(line[1])
        LIS[idx] = line
        dp.append((idx, line[0]))

LIS_LEN = len(LIS)
print(N - LIS_LEN)

last_idx = LIS_LEN - 1
LIS_A = [0] * LIS_LEN

for i in range(len(dp) - 1, -1, -1):
    if dp[i][0] == last_idx:
        LIS_A[last_idx] = dp[i][1]
        last_idx -= 1

for i in range(len(lines_a)):
    if lines_a[i] not in LIS_A:
        print(lines_a[i])
