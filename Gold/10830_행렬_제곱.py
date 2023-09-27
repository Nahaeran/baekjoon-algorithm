N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


def mul_matrix(mat1, mat2, n):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j] % 1000
    return result


def power(mat, b):
    if b == 1:
        return mat
    else:
        temp = power(mat, b // 2)
        if b % 2 == 0:
            return mul_matrix(temp, temp, N)
        else:
            return mul_matrix(mul_matrix(temp, temp, N), mat, N)


result = power(matrix, B)
for line in result:
    print(*map(lambda x: x % 1000, line))
