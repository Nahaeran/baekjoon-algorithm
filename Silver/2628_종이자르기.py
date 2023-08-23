W, H = map(int, input().split())
num_lines = int(input())
h_list = [0]
v_list = [0]

area_list = []

for _ in range(num_lines):
    line_type, num = map(int, input().split())
    if line_type == 0:
        h_list.append(num)
    else:
        v_list.append(num)

h_list.append(H)
v_list.append(W)
h_list.sort()
v_list.sort()

for i in range(1, len(h_list)):
    for j in range(1, len(v_list)):
        width = v_list[j] - v_list[j - 1]
        height = h_list[i] - h_list[i - 1]
        area_list.append(width * height)

print(max(area_list))