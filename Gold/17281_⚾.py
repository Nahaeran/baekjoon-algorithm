def play_inning(player, now_idx, score):
    out = 0
    queue = [0, 0, 0]
    while out < 3:
        if player[now_idx] == 4:
            score += sum(queue) + 1
            queue = [0, 0, 0]
        elif player[now_idx] == 3:
            score += queue[0]
            score += queue[1]
            score += queue[2]
            queue = [1, 0, 0]
        elif player[now_idx] == 2:
            score += queue[0]
            score += queue[1]
            queue = [queue[2], 1, 0]
        elif player[now_idx] == 1:
            score += queue[0]
            queue = [queue[1], queue[2], 1]
        else:
            out += 1
        now_idx += 1
        now_idx %= 9
    return score, now_idx


def get_permutations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i, elem in enumerate(arr):
        for P in get_permutations(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + P]
    if n == 8:
        for per in result:
            per.insert(3, 0)
    return result


N = int(input())
inning_points = [list(map(int, input().split())) for _ in range(N)]
score_list = []

permutation_list = get_permutations(list(range(1, 9)), 8)


#for inning in inning_points:



point_list = []
for permutation in permutation_list:
    score = 0
    now = 0

    sorted_inning = []
    for inning in inning_points:
        point_list = [0] * 9
        for i in range(9):
            idx = permutation.index(i)
            point_list[idx] = inning[i]
        sorted_inning.append(point_list)

    if sorted_inning in point_list:
        continue
    else:
        point_list.append(sorted_inning)

    for inning in sorted_inning:
        score, now = play_inning(inning, now, score)
    score_list.append(score)

print(max(score_list))