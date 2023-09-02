import sys

input = sys.stdin.readline


def play_inning(count):
    global result
    if count == 9:
        start = score = 0
        for inning in inning_points:
            out = 0
            r1, r2, r3 = 0, 0, 0
            while out < 3:
                now_idx = order_list[start]
                if inning[now_idx] == 4:
                    score += r1 + r2 + r3 + 1
                    r1, r2, r3 = 0, 0, 0
                elif inning[now_idx] == 3:
                    score += r1 + r2 + r3
                    r1, r2, r3 = 0, 0, 1
                elif inning[now_idx] == 2:
                    score += r2 + r3
                    r1, r2, r3 = 0, 1, r1
                elif inning[now_idx] == 1:
                    score += r3
                    r1, r2, r3 = 1, r1, r2
                else:
                    out += 1
                start = (start + 1) % 9
        result = max(result, score)
        return

    for i in range(9):
        if selected[i]:
            continue
        selected[i] = 1
        order_list[i] = count
        play_inning(count + 1)
        selected[i] = 0
        order_list[i] = 0


N = int(input())
inning_points = [list(map(int, input().split())) for _ in range(N)]
order_list = [0] * 9
selected = [0] * 9

order_list[3] = 0
selected[3] = 1
result = 0

play_inning(1)
print(result)