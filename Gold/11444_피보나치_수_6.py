import sys
sys.setrecursionlimit(int(1e9))
N = int(input()) - 2
matrix = ((1, 1), (1, 0))
INF = 1000000007


def mul_matrix(mat1, mat2):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j] % INF
    return result


def fib(mat, n):
    if n == 1:
        return mat
    else:
        temp = fib(mat, n // 2)
        if n % 2 == 0:
            return mul_matrix(temp, temp)
        else:
            return mul_matrix(mul_matrix(temp, temp), mat)


if N > 0:
    result = sum(fib(matrix, N)[0])
    print(result % INF)
else:
    print((0, 1, 1)[N + 2])