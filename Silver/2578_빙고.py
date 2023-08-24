def check_bingo(board):
    num_bingo = 0
    for i in range(5):
        r_check = c_check = 0
        for j in range(5):
            if board[i][j] == 0:
                r_check += 1
            if board[j][i] == 0:
                c_check += 1
        if r_check == 5:
            num_bingo += 1
        if c_check == 5:
            num_bingo += 1

    d1_check = d2_check = 0
    for i in range(5):
        if board[i][i] == 0:
            d1_check += 1
        if board[i][4-i] == 0:
            d2_check += 1
    if d1_check == 5:
        num_bingo += 1
    if d2_check == 5:
        num_bingo += 1

    if num_bingo == 3:
        return True
    return False


def find_index(board, e):
    for i in range(5):
        for j in range(5):
            if board[i][j] == e:
                return i, j


bingo = [list(map(int, input().split())) for _ in range(5)]
order = list(map(int, input().split()))
for _ in range(4):
    order.extend(list(map(int, input().split())))

for order_i in range(25):
    i, j = find_index(bingo, order[order_i])
    bingo[i][j] = 0
    if order_i >= 12:
        is_bingo = check_bingo(bingo)
        if is_bingo:
            break
print(order_i+1)