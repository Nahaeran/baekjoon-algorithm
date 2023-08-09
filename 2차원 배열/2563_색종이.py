T = int(input())
cp_list = []
for t in range(1, T + 1):
    cp_list.append(list(map(int, input().split())))
canvas = [[0] * 100 for _ in range(100)]

for cp in cp_list:
    for i in range(cp[0], cp[0] + 10):
        for j in range(cp[1], cp[1] + 10):
            canvas[i][j] = 1

total = 0
for line in canvas:
    total += line.count(1)

print(total)
