W = int(input())
m, n = map(int, input().split())
A = [int(input()) for _ in range(m)]
B = [int(input()) for _ in range(n)]
A *= 2
B *= 2

result = 0
A_sum = []

if sum(A) // 2 <= W:
    for i in range(m):
        for k in range(1, m):
            A_sum.append(sum(A[i:i + k]))
    A_sum.append(sum(A) // 2)
else:
    start = end = 0
    temp = A[start]
    while start < m and end - start < m:
        if temp < W:
            A_sum.append(temp)
            end += 1
            temp += A[end]
        elif temp == W:
            result += 1
            end += 1
            temp += A[end]
        else:
            start += 1
            temp = A[start]
            end = start

B_sum = []

if sum(B) // 2 <= W:
    for i in range(n):
        for k in range(1, n):
            B_sum.append(sum(B[i:i + k]))
    B_sum.append(sum(B) // 2)
else:
    start = end = 0
    temp = B[start]
    while start < n and end - start < n:
        if temp < W:
            B_sum.append(temp)
            end += 1
            temp += B[end]
        elif temp == W:
            result += 1
            end += 1
            temp += B[end]
        else:
            start += 1
            temp = B[start]
            end = start
# print(A_sum, B_sum)
B_sum.sort()

for a in A_sum:
    start = 0
    end = len(B_sum) - 1
    while start <= end:
        mid = (start + end) // 2
        if a + B_sum[mid] == W:
            result += B_sum.count(B_sum[mid])
            break
        elif a + B_sum[mid] < W:
            start = mid + 1
        else:
            end = mid - 1


print(result)


