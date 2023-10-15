def from_top(start, end, temp):
    if end in adj_list[start]:
        return temp
    else:
        for i in range(len(adj_list[start])):
            tmp_s = adj_list[start][i]
            temp += 1
            return from_top(tmp_s, end, temp)


N = int(input())
adj_list = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, c = map(int, input().split())
    adj_list[p].append(c)
    adj_list[c].append(p)

checked = set()
result = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue
        elif frozenset({i, j}) in checked:
            continue
        else:
            if i == 1 or j == 1:
                print(i, j)
                s = 1
                e = max(i, j)
                result += 1
                temp = 0
                result += from_top(s, e, temp)
            else:
                pass
            checked.add(frozenset({i, j}))

# test = set()
# test.add(frozenset({2, 3}))
# print(test)
# print(frozenset({2, 3}) in test)
print(result)
