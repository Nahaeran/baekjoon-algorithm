def bfs(subset, N, a):
    subset_adj = [[0] * N for _ in range(N)]
    for i in subset:
        for j in subset:
            subset_adj[i][j] = adj_matrix[i][j]

    queue = [a]
    visited = [0] * N
    visited[a] = 1
    path = [a]

    while queue:
        t = queue.pop(0)
        for i in range(len(subset_adj[t])):
            if subset_adj[t][i] and not visited[i]:
                queue.append(i)
                path.append(i)
                visited[i] = 1
    for e in subset:
        if e not in path:
            return False
    return True


N = int(input())
Pi = list(map(int, input().split()))
input_adj = [list(map(int, input().split())) for _ in range(N)]
adj_matrix = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(1, len(input_adj[i])):
        idx_i = i
        idx_j = input_adj[i][j] - 1
        adj_matrix[idx_i][idx_j] = 1

all_com = []
for i in range(2**N):
    temp = [[], []]
    for j in range(1 << N):
        if i & 1 << j:
            temp[0].append(j)
        elif j <= N-1:
            temp[1].append(j)
    all_com.append(temp)
all_com.pop(0)
all_com.pop()

result_list = []
for com in all_com:
    cor1 = bfs(com[0], N, com[0][0])
    cor2 = bfs(com[1], N, com[1][0])

    if cor1 and cor2:
        temp1 = temp2 = 0
        for c in com[0]:
            temp1 += Pi[c]
        for c in com[1]:
            temp2 += Pi[c]
        result_list.append(abs(temp1 - temp2))

if result_list:
    print(min(result_list))
else:
    print(-1)