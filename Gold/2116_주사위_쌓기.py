pair = {
    0 : 5,
    1 : 3,
    2 : 4,
    3 : 1,
    4 : 2,
    5 : 0
}


def stack_dice(dice, b):
    b_idx = dice.index(b)
    t_idx = pair[b_idx]
    side = [dice[i] for i in range(6) if i not in [b_idx, t_idx]]
    return max(side), dice[t_idx]


N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(1, 7):
    bottom = i
    temp = 0
    for dice in dices:
        max_side, bottom = stack_dice(dice, bottom)
        temp += max_side
    if result < temp:
        result = temp

print(result)