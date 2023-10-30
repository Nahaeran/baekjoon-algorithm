import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = []
LIS = [arr[0]]


def binary_search(target):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == target:
            return mid
        elif LIS[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start


for i in range(N):
    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
        dp.append((len(LIS) - 1, arr[i]))
    else:
        idx = binary_search(arr[i])
        dp.append((idx, arr[i]))
        LIS[idx] = arr[i]

LIS_LEN = len(LIS)
print(LIS_LEN)

result = [0] * LIS_LEN
idx = LIS_LEN - 1

for i in range(len(dp) - 1, -1, -1):
    if dp[i][0] == idx:
        result[idx] = dp[i][1]
        idx -= 1
print(*result)
