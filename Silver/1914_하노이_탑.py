def hanoi(N, fr, tmp, to):
    if N == 1:
        print(fr, to)
    else:
        hanoi(N - 1, fr, to, tmp)
        print(fr, to)
        hanoi(N - 1, tmp, fr, to)


N = int(input())

num = 2 ** N - 1
print(num)

if N <= 20:
    hanoi(N, 1, 2, 3)