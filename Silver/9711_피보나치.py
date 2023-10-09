import sys
sys.setrecursionlimit(int(1e9))
T = int(input())
matrix = ((1, 1), (1, 0))


def mul_matrix(mat1, mat2):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j] % Q
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

for tc in range(1, T + 1):
    P, Q = map(int, input().split())
    P -= 2
    if P > 0:
        result = sum(fib(matrix, P)[0])
        print(f'Case #{tc}: {result % Q}')
    else:
        print(f'Case #{tc}: {(0, 1, 1)[P + 2] % Q}')
