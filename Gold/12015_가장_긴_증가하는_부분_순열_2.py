import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
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
    else:
        idx = binary_search(arr[i])
        LIS[idx] = arr[i]

print(len(LIS))
print(*LIS)
