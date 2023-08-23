C, R = map(int, input().split())
num = int(input())

if num > C * R:
    print(0)
else:
    seat = 1
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    i = j = 1
    k = 0
    seats = [[0] * (C + 1) for _ in range(R + 1)]
    seats[i][j] = seat
    while seat != num:
        ni = i + di[k]
        nj = j + dj[k]
        if 0 < ni <= R and 0 < nj <= C and not seats[ni][nj]:
            seat += 1
            seats[i][j] = seat
            i, j = ni, nj
        else:
            k = (k + 1) % 4
    print(j, i)