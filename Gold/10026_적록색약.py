from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())

graph = [input() for _ in range(N)]
graph_rg = list(map(lambda x: x.replace('G', 'R'), graph))

cnt1 = cnt2 = 0

visited = [[False] * N for _ in range(N)]
visited_rg = [[False] * N for _ in range(N)]


def bfs(v, g, visit):
    q = deque([v])
    visit[v[0]][v[1]] = True
    while q:
        v = q.popleft()
        for k in range(4):
            ni = v[0] + di[k]
            nj = v[1] + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and g[v[0]][v[1]] == g[ni][nj]:
                q.append([ni, nj])
                visit[ni][nj] = True


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs([i, j], graph, visited)
            cnt1 += 1
        if not visited_rg[i][j]:
            bfs([i, j], graph_rg, visited_rg)
            cnt2 += 1


print(cnt1, cnt2)