import sys

N = int(sys.stdin.readline())
x_list = [0] * N
y_list = [0] * N

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_list[i] = x
    y_list[i] = y

x_list.append(x_list[0])
y_list.append(y_list[0])

result = 0
for i in range(N):
    result += 0.5 * (x_list[i] * y_list[i + 1])
    result -= 0.5 * (x_list[i + 1] * y_list[i])

print(abs(round(result, 1)))
