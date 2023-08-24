N = int(input())
input_list = [0] * N

for i in range(N):
    input_list[i] = list(map(int, input().split()))

input_list.sort(key=lambda x: x[0])
max_pillar = max(input_list, key=lambda x: x[1])
max_pillar_idx = input_list.index(max_pillar)

area = 0
idx = input_list[0][0]
h = input_list[0][1]
for p in input_list[:max_pillar_idx + 1]:
    if h <= p[1]:
        area += h * (p[0] - idx)
        idx = p[0]
        h = p[1]

idx = input_list[-1][0]
h = input_list[-1][1]
right = input_list[:max_pillar_idx:-1]
right.append(max_pillar)
for p in right:
    if h <= p[1]:
        area += h * (idx - p[0])
        idx = p[0]
        h = p[1]

area += max_pillar[1]
print(area)