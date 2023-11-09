import sys

A, B = map(int, sys.stdin.readline().split())
one_sum = [0 for _ in range(60)]


def count(num):
    cnt = 0
    bin_num = bin(num)[2:]
    length = len(bin_num)
    for i in range(length):
        if bin_num[i] == '1':
            val = length - i - 1
            cnt += one_sum[val]
            cnt += (num - 2 ** val + 1)
            num = num - 2 ** val
    return cnt


for i in range(1, 60):
    one_sum[i] = 2 ** (i - 1) + 2 * one_sum[i - 1]

print(count(B) - count(A - 1))
