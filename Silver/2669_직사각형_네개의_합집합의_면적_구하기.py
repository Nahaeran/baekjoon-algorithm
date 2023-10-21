boxes = [list(map(int, input().split())) for _ in range(4)]
plane = [[0] * 100 for _ in range(100)]

for box in boxes:
    for x in range(box[0], box[2]):
        for y in range(box[1], box[3]):
            plane[x][y] = 1
area = 0
for line in plane:
    area += line.count(1)
print(area)