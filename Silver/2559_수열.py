N, K = map(int, input().split())
li = list(map(int, input().split()))

l_idx = r_idx = 0
temp = li[0]
result = sum(li[0:K])
while r_idx != N:
    if r_idx - l_idx < K-1:
        r_idx += 1
        temp += li[r_idx]
    elif r_idx - l_idx > K-1:
        temp -= li[l_idx]
        l_idx += 1
    else:
        if result < temp:
            result = temp
        r_idx += 1
        if r_idx != N:
            temp += li[r_idx]

print(result)