import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = 100001
l_idx = r_idx = 0
temp_sum = arr[l_idx]

while l_idx < N:
    if r_idx == N - 1 and temp_sum < S:
        break
    elif temp_sum < S and r_idx < N - 1:
        r_idx += 1
        temp_sum += arr[r_idx]
    elif temp_sum >= S and r_idx < N:
        result = min(result, r_idx - l_idx + 1)
        temp_sum -= arr[l_idx]
        l_idx += 1

if result == 100001:
    result = 0
print(result)
