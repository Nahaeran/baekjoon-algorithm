n, K = map(int, input().split())

bit_n = bin(n)
cnt = bit_n.count("1")
buy = 0

while cnt > K:
    buy += 1
    n += 1
    bit_n = bin(n)
    cnt = bit_n.count("1")

print(buy)