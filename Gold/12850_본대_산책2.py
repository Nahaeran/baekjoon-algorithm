import sys

D = int(sys.stdin.readline())
campus = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0]
]
INF = 1000000007


def mul(mat1, mat2):
    result = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                result[i][j] += mat1[i][k] * mat2[k][j] % INF
    return result


def matrix_mul(mat, n):
    if n == 1:
        return mat
    else:
        temp = matrix_mul(mat, n // 2)
        if n % 2 == 0:
            return mul(temp, temp)
        else:
            return mul(mul(temp, temp), mat)


print(matrix_mul(campus, D)[0][0] % INF)
