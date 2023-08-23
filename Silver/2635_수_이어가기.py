N = int(input())

max_len = 2
max_list = []

for i in range(1, N + 1):
    a = [N, i]
    next = a[-2] - a[-1]
    a.append(next)

    while a[-2] >= a[-1]:
        next = a[-2] - a[-1]
        a.append(next)

    if max_len < len(a):
        max_len = len(a)
        max_list = a

print(max_len)
print(*max_list)