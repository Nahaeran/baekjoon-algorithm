def find_best(arr, n):
    l_idx = 0
    r_idx = n - 1
    neutral = abs(arr[l_idx] + arr[r_idx])

    for i in range(n - 1):
        curr = arr[i]

        start = i + 1
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            temp = curr + arr[mid]

            if neutral > abs(temp):
                neutral = abs(temp)
                l_idx = i
                r_idx = mid

            if temp < 0:
                start = mid + 1
            else:
                end = mid - 1

    return arr[l_idx], arr[r_idx]


N = int(input())
input_li = list(map(int, input().split()))
print(*find_best(input_li, N))