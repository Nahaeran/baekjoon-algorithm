N = int(input())
c_papers = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * 1001 for _ in range(1001)]
nums = [0] * N

for p in range(len(c_papers)):
    y, x, w, h = c_papers[p]
    for i in range(x, x+h):
        for j in range(y, y+w):
            board[i][j] = p + 1

for p in range(len(c_papers)):
    y, x, w, h = c_papers[p]
    num = 0
    for i in range(x, x + h):
        for j in range(y, y + w):
            if board[i][j] == p + 1:
                num += 1
    nums[p] = num

for i in range(N):
    print(nums[i])